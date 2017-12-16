#!/usr/bin/ruby

require 'nokogiri'
require 'socket'

# open targets.txt file
targets = File.open('targets.txt').read

# do masscan
targets.each_line do |line|
    target = line.chomp
    if (target =~ /^[a-zA-Z]/) # check if target starts with a character
        ip = IPSocket::getaddress(target) # masscan requires an IP address
        puts "\nRunning masscan on IP address #{ip}..."
        system("masscan --open -sS -p 0-65535 #{ip} --rate=10000 -oX #{ip.gsub("/", "_")}masscan.xml 1>&2")
    else
        puts "\nRunning masscan on IP address #{target}..."
        system("masscan --open -sS -p 0-65535 #{target} --rate=10000 -oX #{target.gsub("/", "_")}.masscan.xml 1>&2")
    end
end

$ip_array = Array.new
$port_array = Array.new
# read in hosts and ports from masscan xml
masscan_xml_files = Dir.glob("*.masscan.xml")
masscan_xml_files.each do |file|
        xml_file = File.read(file)
    doc = Nokogiri::XML.parse(xml_file)
    doc.xpath('//address').each do |x|
        $ip_array << x.values[0]
    end
    doc.xpath('//port').each do |x|
        $port_array << x.values[1]
    end
end

$ip_array.uniq!
$port_array.uniq!

IO.write("nmap_targets.txt", $ip_array.join("\n"))

puts ("\nRunning nmap scan...")
system("nmap -sS -Pn -sV -p #{$port_array.join(',')} --open -oA nmap_TCP_scan -iL nmap_targets.txt 1>&2")
system("nmap -sU --top-ports 100 -oA nmap_UDP_scan -iL nmap_targets.txt 1>&2")
puts ("\nNmap scan complete!")




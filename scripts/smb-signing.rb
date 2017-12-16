#!/usr/bin/ruby
require 'nmap/xml'

puts "Message Signing Disabled:"
Nmap::XML.new(ARGV[0]) do |xml|
  xml.each_host do |host|
    #puts "\n"
    #print "#{host.ip}"

    host.scripts.each do |name,output|
      output.each_line { |line| puts "#{host.ip}" if line.include? 'disabled'}
    end
  end
end


#!/usr/bin/ruby

require 'nokogiri'
require 'open-uri'

filetypes = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'vsd', 'vsdx']
search_results = Array.new
exiftool_users = Array.new


system("mkdir #{ARGV[0]}")

filetypes.each do |ext|
  search_url = "http://www.google.com/search?num=100&q=filetype:#{ext}+site:#{ARGV[0]}"
  page = Nokogiri::HTML(open(search_url))
  page.search("cite").each do |cite|
  search_results << cite.inner_text if (cite.inner_text =~ /\.#{ext}$/)
  end
end

search_results.each do |result|
	system("wget #{result} -P #{ARGV[0]}")
end

filetypes.each do |ext|
	exiftool_output = `exiftool #{ARGV[0]}/*.#{ext} | tr -s ' ' | egrep 'Creator|Last Modified By' | grep -v 'Microsoft' | grep -v 'Adobe'`
	exiftool_output.each_line do |line|
		exiftool_users << line.split(': ')[1]
	end
end

puts "Users found:"
exiftool_users.each do |user|
	puts user unless user.empty?
end
				
#!/usr/bin/ruby

require 'nokogiri'
require 'open-uri'
require 'uri'


system("mkdir #{ARGV[0]}-metadata")

filetypes.each do |ext|
  site_search = "http://www.google.com/search?num=100&q=site:#{ARGV[0]}"
  page = Nokogiri::HTML(open(search_url))
  page.search("cite").each do |cite|
  search_results << cite.inner_text if (cite.inner_text =~ /\.#{ext}$/)
  end
end

				

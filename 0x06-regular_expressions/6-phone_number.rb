#!/usr/bin/env ruby

# This script  has a regular expression that matches a 10 digit phone number
puts ARGV[0].scan(/^\d{10,10}$/).join


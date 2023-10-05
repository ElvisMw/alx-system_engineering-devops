#!/usr/bin/env ruby

# This script outputs: [SENDER-name or number],[RECEIVER-name or number],[FLAGS]
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")


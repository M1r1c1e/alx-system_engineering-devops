#!/usr/bin/env ruby
# This script searches log files and outputs the [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(",")

#!/usr/bin/env ruby

# Checking if input CSV file is provided as an argument
unless ARGV.length == 1
  puts "Usage: #{$PROGRAM_NAME} <input_csv_file>"
  exit 1
end

# Input the CSV file
input_file = ARGV[0]

# Checking if the input file exists
unless File.exist?(input_file)
  puts "Error: Input file '#{input_file}' not found."
  exit 1
end

# Output header
puts "Sender,Receiver,Flags"

# Process CSV file and retreive relevant information
File.foreach(input_file) do |line|
  sender, receiver, flags = line.chomp.split(',')
  puts "#{sender},#{receiver},#{flags}"
end

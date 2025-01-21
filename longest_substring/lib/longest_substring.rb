# @param {String} s
# @return {Integer}

def eliminate_successive_equal_substrings(input_string, substring)
  new_string = +substring
  for substr in input_string.chars.each_slice(substring.length).map(&:join)[1..-1]
     if substr != substring
      new_string += substr
     end
  end
  return new_string
end

def length_of_longest_substring(s)
  input_string = +s

  if(input_string.length <= 1)
    return input_string.length
  end

  longest = 0

  while input_string.length > 0
    substring = ""
    c = 0
    equal_last = false
    for i in input_string.chars
      if substring.include? i
        equal_last = substring[-1] == i
        break
      end
      substring += i
      c += 1
    end
    
    if substring.length > longest
      longest = substring.length
    end


    if equal_last
      input_string = input_string[c..-1]
    else
      total_substrings = input_string.scan(substring).length
      input_string = eliminate_successive_equal_substrings(input_string, substring)

      if total_substrings <= 1
        input_string[0] = ""
      end
    end


  end

  return longest
end

print(length_of_longest_substring("ggububgvfk"))

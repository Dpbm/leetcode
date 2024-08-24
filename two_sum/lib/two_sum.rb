# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  index_range = (0..nums.length-1).to_a
  if(target > 0 && target > nums.last) || (target < 0 && target < nums.last)
    index_range = index_range.reverse
  end
  # print index_range
  # print nums
  # print "\n"
  for i in index_range do
    first_val = nums[i]
    
    for j in index_range do
      if i == j
        next
      end
      second_val = nums[j]
      # print "first " << first_val.to_s << " second " << second_val.to_s << " i=" << i.to_s << " j=" << j.to_s << " \n"
      if first_val+second_val == target
        # print "i=" << i.to_s << " j=" << j.to_s << "\n\n"
        
        return [i,j].sort 
      end
    end
  end
        print "\n\n"
  return [nil, nil]
end

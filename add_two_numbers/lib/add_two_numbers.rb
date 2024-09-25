class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end

#@param {ListNode} l1
#@param {ListNode} l2
#@return {ListNode}


def add_two_numbers(l1, l2)
  final_sum = 0  
  for node in [l1, l2] do
    i = 0
    parts = []
    while node != nil do
      parts.push([node.val, i])
      i += 1
      node = node.next
    end


    final_val = 0
    for part in parts do
        val = part[0]
        factor = 10**part[1]
        final_val += val*factor
    end
    final_sum += final_val
  end


  if final_sum == 0
    return ListNode.new
  end


  first_node = nil
  last_node = nil
  actual_node = nil

  while final_sum > 0
    val = final_sum % 10
    
     if actual_node == nil
       first_node = ListNode.new
       first_node.val = val

       actual_node = first_node
       last_node = first_node
     else
      actual_node = ListNode.new
      actual_node.val = val
      last_node.next = actual_node
      last_node = actual_node
     end 

    final_sum /= 10
  end
  
  return first_node
end

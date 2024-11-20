from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def updateActualNode(self, newVal:int, actualNode:Optional[ListNode]) -> ListNode:
        if(actualNode == None):
            return ListNode(val=newVal)
        
        new_node = ListNode(val=newVal)
        actualNode.next = new_node
        return new_node



    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None and list2 == None):
            return None
        elif(list1 != None and list2 == None):
            return list1
        elif(list1 == None and list2 != None):
            return list2
       
        base_node = None
        actual_node = None

        actual1 = list1
        actual2 = list2

        while(actual1 != None or actual2 != None):
            new_node_val = 0

            #check nones
            has_none = None in [actual1, actual2]
            node_not_none = actual1 if actual2 == None else actual2

            if(has_none):
                while node_not_none != None:
                    actual_node = self.updateActualNode(node_not_none.val, actual_node)
                    node_not_none = node_not_none.next
            
                    if(base_node == None):
                        base_node = actual_node

                break



            if(actual1.val <= actual2.val):
                new_node_val = actual1.val
                actual1 = actual1.next

            else:
                new_node_val = actual2.val
                actual2 = actual2.next

            actual_node = self.updateActualNode(new_node_val, actual_node);
            if(base_node == None):
                base_node = actual_node

        return base_node

if __name__ == "__main__":
    sol = Solution()

    zero_node = ListNode()

    assert sol.mergeTwoLists(None, None) == None, "Failed #1"
    assert sol.mergeTwoLists(None, zero_node) == zero_node, "Failed #2"
    assert sol.mergeTwoLists(zero_node, None) == zero_node, "Failed #3"

    list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
    list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
    result = sol.mergeTwoLists(list1, list2)
    merged_list = []
    while result != None:
        merged_list.append(result.val)
        result = result.next
    assert merged_list == [1,1,2,3,4,4], "Failed #4"


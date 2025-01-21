struct Solution{
}

impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
       let mut c_digits = digits.clone();
       let mut index = digits.len()-1;

       loop{
            let _sum = c_digits[index] + 1;

            if _sum <= 9 {
                c_digits[index] = _sum;
                break;
            }

            c_digits[index] = 0;
            if index == 0{
                c_digits.insert(0,1);
                break;
            }

            index -= 1;
       }


        
        c_digits
    }
}

fn main() {
    assert!(Solution::plus_one(vec![1,2,3]) == [1,2,4]);
    assert!(Solution::plus_one(vec![4, 3, 2, 1]) == [4,3,2,2]);
    assert!(Solution::plus_one(vec![9]) == [1,0]);
}

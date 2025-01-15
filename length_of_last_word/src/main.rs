struct Solution{}

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let split_s:Vec<&str> = s.rsplit(' ').collect();

        for i in split_s{
            match i {
                "" => continue,
                _ => return i.len().try_into().unwrap()
            }
        }
        0
    }
}

fn main() {
    assert!(Solution::length_of_last_word("Hello World".to_string()) == 5);
    assert!(Solution::length_of_last_word("   fly me   to   the moon  ".to_string()) == 4);
    assert!(Solution::length_of_last_word("luffy is still joyboy".to_string()) == 6);
}

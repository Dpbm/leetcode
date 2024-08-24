# frozen_string_literal: true

require "test_helper"
require "set"

class TestTwoSum < Minitest::Test
  def test_first_case
    assert two_sum([2,7,11,15], 9).to_set == Set[0,1]
  end
  def test_second_case
    assert two_sum([3,2,4], 6).to_set == Set[1,2]
  end
  def test_third_case
    assert two_sum([3,3], 6).to_set == Set[0,1]
  end
  def test_forth_case
    assert two_sum([5, 10, 12, 35, 43, 99, 140], 47).to_set == Set[2,3]
  end
  def test_fifth_case
    assert two_sum([1, 2, 3, 3, 4, 5, 6, 6, 9, 10, 15, 2222, 33333, 5555], 2223).to_set == Set[0, 11]
  end
  def test_sixth_case
    assert two_sum([-1, -2, -3, -4, -5], -8).to_set == Set[2, 4]
  end
end

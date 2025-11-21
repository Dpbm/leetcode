#include <print>
#include <tuple>
#include <vector>


class Solution {

private:
    double get_median_even(int num1, int num2) { return (num1 + num2) / 2; }

    bool should_use_even_median(int m, int n) { return (m + n) % 2 == 0; }

    tuple<int, int> get_middle_points(int m, int n) {
        int total = m + n;
        int middle_point = (int)total / 2;

        return make_tuple(middle_point - 1, middle_point);
    }

    bool is_in_the_first_array(int m, int pos) { return pos <= m - 1; }

    int get_middle_point(int m, int n) { return ((int)((m + n) / 2)); }

    bool is_out_of_bounds(int max, int i) { return i >= max; }

    double single_side(vector<int>& array, int m, int n){
        bool use_even = this->should_use_even_median(m, n);
        if(use_even){
            int pointB = (int)(n/2);
            int pointA = pointA-1;

            return (array[pointA]+array[pointB])/2;
        }

        return array[(int)n/2];
    }


public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        size_t m = nums1.size();
        size_t n = nums2.size();


        if(m == 0){
            return this->single_side(nums2, m, n);
        }

        if(n == 0){
            return this->single_side(nums1, m,n);
        }

        bool use_even = this->should_use_even_median(m, n);



        if (nums1[m - 1] <= nums2[0]) {

            if (use_even) {

                auto points = get_middle_points(m, n);
                int first_point = get<0>(points);
                int second_point = get<1>(points);

                double total = 0;

                // [1,2] [3,4,5,6]
                // indexes 2 and 3

                // it's in the first array
                total += this->is_in_the_first_array(m, first_point)
                             ? nums1[first_point]
                             : nums2[first_point - m];
                total += this->is_in_the_first_array(m, second_point)
                             ? nums1[second_point]
                             : nums2[second_point - m];

                return total / 2;
            }

            int middle_point = get_middle_point(m, n);
            return this->is_in_the_first_array(m, middle_point)
                       ? nums1[middle_point]
                       : nums2[middle_point - m];
        } 

        int last_pos =
            use_even ? get<1>(get_middle_points(m, n)) : get_middle_point(m, n);

        int array_size = last_pos+1;
        vector<double> tmp_values;

        int nums1_pointer = 0;
        int nums2_pointer = 0;

        while (tmp_values.size() < array_size) {

            while (!this->is_out_of_bounds(m,nums1_pointer) && nums1[nums1_pointer] < nums2[nums2_pointer]) {
                tmp_values.push_back(nums1[nums1_pointer]);
                nums1_pointer++;
            }


            if(this->is_out_of_bounds(m,nums1_pointer)){
                while(!this->is_out_of_bounds(n,nums2_pointer) && tmp_values.size() < array_size){
                    tmp_values.push_back(nums2[nums2_pointer++]);
                }
                break;
            }


            while (!this->is_out_of_bounds(n,nums2_pointer) && nums2[nums2_pointer] < nums1[nums1_pointer]) {
                tmp_values.push_back(nums2[nums2_pointer]);
                nums2_pointer++;
            }

        }


        #ifdef DEBUG
            for(int c : tmp_values){
                printf("%d ",c);
            }
            printf("\n");
        #endif



        return use_even ? (tmp_values[last_pos] + tmp_values[last_pos - 1]) / 2
                        : tmp_values[last_pos];
    }
};

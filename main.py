import _1_contain_duplicate
import _2_valid_anagram
import _3_two_sum
import _4_group_anagram
import _8_valid_sudoku
import _11_two_sum_2_input_array_is_sorted
import _12_3sum
import _10_valid_palindrome
import _15_best_time_to_buy_and_sell_stock
import _13_container_with_most_water
import _11_two_sum_2_input_array_is_sorted

if __name__ == "__main__":
    sol = _11_two_sum_2_input_array_is_sorted.Solution()
    numbers = [2, 3, 4]
    target = 6
    result = sol.twoSum(numbers, target)

    print(f"결과: {result}")

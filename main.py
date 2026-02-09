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
import _14_trapping_rain_water
import _16_valid_parentheses
import _17_minstack

if __name__ == "__main__":
    sol = _8_valid_sudoku.Solution()
    p = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    res = sol.isValidSudoku(p)
    print(res)
    # minStack.getMin() # return 0
    # minStack.pop()
    # minStack.top()
    # minStack.getMin()



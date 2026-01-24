import _1_contain_duplicate
import _2_valid_anagram
import _3_two_sum
import _4_group_anagram
import _8_valid_sudoku
import _9_longest_consecutive_sequence

if __name__ == "__main__":
    sol = _9_longest_consecutive_sequence.Solution()

    nums = [2, 20, 4, 10, 3, 4, 5]

    result = sol.longestConsecutive(nums)
    print(f"결과: {result}")

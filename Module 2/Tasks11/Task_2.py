class Mathematician:
    pass

    def square_nums(self, nums: list) -> list:
        squared = [i ** 2 for i in nums]
        return squared

    def remove_positives(self, nums: list) -> list:
        positives = [i for i in nums if i <= 0]
        return positives

    def filter_leaps(self, nums: list) -> list:
        leap_year = []
        for i in range(len(nums)):
            if nums[i] % 4 == 0:
                if nums[i] % 100 == 0:
                    if nums[i] % 400 == 0:
                        leap_year.append(nums[i])
                    else:
                        pass
                else:
                    leap_year.append(nums[i])
            else:
                pass
        return leap_year


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
print(m.square_nums([7, 11, 5, 4]), [49, 121, 25, 16])
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
print(m.remove_positives([26, -11, -8, 13, -90]), [-11, -8, -90])
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]), [1884, 2020])

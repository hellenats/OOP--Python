# my_d = {1: "1", 2: "2"}
#
# print(my_d.items())


# from itertools import permutations
#
#
# lst = [1, 2, 3]
# for perm in permutations(lst):
#     print(perm)
#
# class RoyalZone:
#     @property
#     def formatted_name(self):
#         res = ''
#         for word in self.__class__.__name__:
#             if word.isupper() and res:
#                 res += " "
#             res += word
#         return res
#
# # Create an instance of the class
# rz = RoyalZone()
#
# # Access the formatted name
# print(rz.formatted_name)
# print(rz.__class__.__name__)

value = "       "

if len(value.strip()) < 3:
    raise ValueError("Product model must be at least 3 chars long!")
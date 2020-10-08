# import matplotlib.pyplot as plt
#
# date = [' 06/09/2020','07/09/2020','08/09/2020','09/09/2020','10/09/2020','11/09/2020','12/09/2020']
# temp_max_c = [24.9,27.8,29.6,28.8,29.1,31.0,23.0]
# temp_min_c = [21.7,20.0,20.6,20.6,23.0,23.0,17.0]
#
# plt.plot(date,temp_max_c,'b-',label = 'max temp')
# plt.plot(date,temp_min_c,'r--',label = 'min temp')
#
# plt.legend()
#
# plt.xlabel('date')
# plt.ylabel('temp max and min in c')
#
# plt.title('Line graph!')
#
# plt.show()
def isPalindrome(s):
    return s if s == s[::-1] else None

print(isPalindrome('ram'))

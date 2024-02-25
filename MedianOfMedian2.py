list_a = [28, 14, 13, 21, 19, 27, 23, 30, 16, 3]

def median_of_median(arr):
    
    def bubble_sort(sublist):
        n = len(sublist)
        for i in range(n):
            for j in range(0, n-i-1):
                if sublist[j] > sublist[j+1]:
                    sublist[j], sublist[j+1] = sublist[j+1], sublist[j]

    # หาค่ามัธยฐานของแต่ละ sublist
    sublists = [sorted(arr[i:i+3]) for i in range(0, len(arr), 3)]
    
    # หาค่ามัธยฐานของค่ามัธยฐานของแต่ละ sublist
    median_of_medians = []
    for sublist in sublists:
        bubble_sort(sublist)
        sublist_median = sublist[0]  # เนื่องจาก sublist มีขนาดเท่ากับ 3 จะมีค่ามัธยฐานที่ index 1
        median_of_medians.append(sublist_median)

    # หาค่ามัธยฐานของค่ามัธยฐาน
    bubble_sort(median_of_medians)
    median = median_of_medians[1]  # เนื่องจาก median_of_medians มีขนาดเท่ากับ 3 จะมีค่ามัธยฐานที่ index 1
    
    return median

print("Output:", median_of_median(list_a))  # แสดงผลลัพธ์

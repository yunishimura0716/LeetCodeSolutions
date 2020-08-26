class Solution:
    def reformatDate(self, date: str) -> str:
        month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_dict = {month_list[i]: "{}".format(i+1) for i in range(len(month_list))}
        date_list = date.split(" ")
        
        day = date_list[0][:-2].zfill(2)
        month = month_dict[date_list[1]].zfill(2)
        year = date_list[2]
        
        return "{}-{}-{}".format(year, month, day)

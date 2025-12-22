# Bai 6
# Colored Ribbon
class Ribbon:
    def __init__(self, color_code, length):
        self.color_code = color_code
        self.length = length
        
        
class RibbonCollector:
    def __init__(self):
        self.ribbons = []
        
    def add_ribbon(self, ribbon):
        self.ribbons.append(ribbon)
        
    def tracking_ribbons(self):
        tracking_info = {}
        for ribbon in self.ribbons:
            color = ribbon.color_code
            length = ribbon.length
            if color not in tracking_info:
                tracking_info[color] = {"total_length": 0, "count": 0}

            tracking_info[color]["total_length"] += length
            tracking_info[color]["count"] += 1

        return tracking_info

num_of_ribbons = int(input())
collector = RibbonCollector()

for _ in range(num_of_ribbons):
    color_code, length = map(int, input().split())
    ribbon = Ribbon(color_code, length)
    collector.add_ribbon(ribbon)

tracking_info = collector.tracking_ribbons()    

print(len(tracking_info))
# sorted by color code
for color, info in sorted(tracking_info.items()):
    print(f"{color} {info['total_length']} {info['count']}")

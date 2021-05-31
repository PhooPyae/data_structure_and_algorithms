def find_area(width, high):
    return width * high

def find_start(start, height):
    if height[start+1] > height[start]:
        return height[start+1] , start+1
    else:
        return height[start] , start

def find_end(end, height):
    if height[end-1] > height[end]:
        return height[end-1] , end-1
    else:
        return height[end] , end

def maxArea(height):
    start = height[0]
    area = 0
    start_index = 0
    end = height[len(height)-1]
    end_index = len(height) - 1
    start_width = start_index
    end_width = end_index

    if len(height) == 2:
        return find_area(1, min(start,end))

    while start_index < end_index:
        if start_index == 0:
            h = min(start,end)
            w = end_index - start_index
            area = find_area(w,h)
        
        tmp_area_1 = find_area(end_width-start_index, min(height[start_index],height[end_width]))
        tmp_area_2 = find_area(end_index-start_width, min(height[start_width],height[end_index]))
        if tmp_area_1 > area:
            area = tmp_area_1
        elif tmp_area_2 > area:
            area = tmp_area_2

        tmp_start, i = find_start(start_width, height)
        tmp_end, j = find_end(end_width, height)
        h = min(tmp_start, tmp_end)
        w = j - i
        tmp_area = find_area(w,h)

        if tmp_area > area:
            area = tmp_area
            start = tmp_start
            end = tmp_end
            start_width = i
            end_width = j
        start_index += 1
        end_index -= 1
    return area

if __name__ == '__main__':
    height = [1,8,6,2,555,4444,8,3,7]
    print(maxArea(height))
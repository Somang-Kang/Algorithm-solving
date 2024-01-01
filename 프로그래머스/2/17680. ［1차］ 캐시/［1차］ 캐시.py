def solution(cacheSize, cities):
    city_list = []
    cnt = 0
    if cacheSize==0:
        return 5*len(cities)
    
    for city in cities:
        city = city.upper()
        
        if city in city_list:
            cnt+=1
            city_list.remove(city)
            city_list.append(city)
        else:
            cnt+=5
            if len(city_list)<cacheSize:
                city_list.append(city)
            else:    
                city_list.pop(0)
                city_list.append(city)
    
    return cnt
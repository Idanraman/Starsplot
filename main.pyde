def setup():
    size_c = 500
    center = size_c/2
    size(500,500)
    background(0)
    
    dots_count = 125
    dis_to_connect = 50
    keep_lonely_dots = False
    name = "1"
    
    stroke(255,255,255)
    per_row = int(sqrt(dots_count))
    delta = int(size_c/per_row)
    dotslocs = [[-10000,-10000]]*dots_count
    
    dotscreated = 0
    for x in range(per_row):
        for y in range(per_row):
            if random(100)>20:
                xcord = random(delta) + size_c*0.03 + x*delta *0.94
                ycord = random(delta) + size_c*0.03 + y*delta*0.94
                dotslocs[dotscreated] = [xcord,ycord]
                dotscreated +=1
    
    for loc in dotslocs:
        found_partner = False
        for loc2 in dotslocs:
            distance = (loc[0]-loc2[0])**2 + (loc[1]-loc2[1])**2
            if distance < dis_to_connect**2 and distance > 0:
                line(loc[0], loc[1], loc2[0], loc2[1])
                found_partner = True
        if found_partner or keep_lonely_dots:
                ellipse(loc[0], loc[1], 10, 10)

saveloc = "Examples/" + name + ".png"
save(saveloc)
dan_text = """Advertising companies say advertising is necessary and important. 
It informs people about new products. Advertising hoardings in the street make our environment colorful.
And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. 
Advertising can educate, too. 
Adverts tell us about new, healthy products. 
And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful.
 Without advertising, life is boring and colorless.
But some consumers argue that advertising is a bad thing. 
They say that advertising is bad for children. 
Adverts make children ‘pester’ their parents buy things for them. 
Advertisers know we love our children and want to give them everything.
 So they use children’s ‘pester power’ to sell their products. 
Finally, consumers say, if there is advertising there must be rules. 
Some adverts advertise unhealthy things like cigarettes and make people waste their money."""

def func():
    count = 0
    for i in dan_text:
        if 's' and 't' in dan_text:
            count += 1
    print(count)

func()

def function(dan_text):
    dan_text.lower()
    for j in dan_text.split():
        if j.startswith('advert'):
            j = j.upper()
            print(j)

    
       
function(dan_text)

# On the twelfth day of Christmas, my true love sent to me
# Twelve drummers drumming
# Eleven pipers piping
# Ten lords a-leaping
# Nine ladies dancing
# Eight maids a-milking
# Seven swans a-swimming
# Six geese a-laying
# Five golden rings
# Four calling birds
# Three french hens
# Two turtle doves, and
# A partridge in a pear tree
import ex089

phrases = {
    1: "A partridge in a pear tree,",
    2: "Two turtle doves,",
    3: "Three french hens,",
    4: "Four calling birds,",
    5: "Five golden rings,",
    6: "Six geese a-laying,",
    7: "Seven swans a-swimming,",
    8: "Eight maids a-milking,",
    9: "Nine ladies dancing,",
    10: "Ten lords a-leaping,",
    11: "Eleven pipers piping,",
    12: "Twelve drummers drumming,",
}

done = [""]


for k, v in phrases.items():
    print(
        f"On the {ex089.convert(k - 1)} day of Christmas My true love sent to me, {v}",
        end="",
    )
    for items in done:
        print(items)
    print(end="\n")
    done.insert(1, v)

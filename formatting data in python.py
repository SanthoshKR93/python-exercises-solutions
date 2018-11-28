def formatt(idict,lj,rj):
    print('food items'.center(lj+rj,'*'))
    for k,v in idict.items():
        print(k.ljust(lj,'.')+str(v).rjust(rj))
fooditems ={'porotta':10,'chapathi':10,'dosa':10}
formatt(fooditems,12,5)
formatt(fooditems,20,6)


from Tests import com
import Tests.pops as pops

if __name__ == '__main__':
    main_p = pops.pop_c()
    i1 = pops.new_ind()
    i1.ID = 1
    i2 = pops.new_ind()
    i2.ID = 2

    main_p.members.append(i1)
    main_p.members.append(i2)
    for a in range(0, 100):
        main_p.tick(True)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

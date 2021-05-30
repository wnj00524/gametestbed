from Tests import com
import Tests.pops as pops

if __name__ == '__main__':
    main_p = pops.population()
    main_p.add_individual(1)
    main_p.add_individual(1)
    main_p.add_individual(1)
    main_p.add_individual(1)
    main_p.add_individual(1)

    for a in range(0, 100):
        main_p.tick()
    print(main_p.members[0].needs["hunger"])






# See PyCharm help at https://www.jetbrains.com/help/pycharm/

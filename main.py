from Tests import com
import Tests.pops as pops
#import Tests.gui
import  Tests.records as Records


if __name__ == '__main__':
    main_p = pops.population()
    main_p.add_individual(1)
    main_p.add_individual(1)
    main_p.add_individual(1)
    main_p.add_individual(1)
    main_p.add_individual(1)
    r1 = Records.Record_Person()
    g1 = Records.Record_Group()
    l1 = Records.Record_Location()
    l1.value = "Twitter"

    l1.link_person(r1)
    r1.first_name = "Bob"
    r1.last_name = "Stone"
    g1.name = "First Group"
    print(type(r1))
    for loc in r1.linked_locations:
        print(loc.value)













#    for a in range(0, 100):
 #       main_p.tick(True)
  #  print(main_p.members[0].needs["hunger"])








# See PyCharm help at https://www.jetbrains.com/help/pycharm/

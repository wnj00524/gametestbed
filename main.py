from Tests import com
import Tests.pops as pops
#import Tests.gui
import  Tests.records as Records


if __name__ == '__main__':
    r1 = Records.Record_Person()
    a1 = Records.Record_Online_ID()
    l1 = Records.Record_Location()
    g1 = Records.Record_Group()

    r1.first_name = "Bob"
    r1.last_name = "Bobson"
    a1.value = "bob@bobson.com"
    l1.value = "Twitter"
    g1.name = "Microsoft"

    r1.link_online_alias(a1)
    r1.link_location(l1)
    r1.link_group(g1)

    print(r1.search_names("bob"))
    print(r1.search_alias(("bob")))
    print(r1.search_locations("twitter"))














#    for a in range(0, 100):
 #       main_p.tick(True)
  #  print(main_p.members[0].needs["hunger"])








# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is to solve day #01 of the Advent of Code 2020
https://adventofcode.com/2020/day/1


These are the details:
"Before you leave, the Elves in accounting just need you to 
fix your expense report (your puzzle input); 
apparently, something isn't quite adding up.

Specifically, they need you to find the two entries 
that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. 
Multiplying them together produces 1721 * 299 = 514579, 
so the correct answer is 514579.

Of course, your expense report is much larger. 
Find the two entries that sum to 2020; 
what do you get if you multiply them together?



"""



import numpy as np

# Data needs to be loaded to the text file before
c= np.loadtxt('advent_day1.txt') 

print (len(c))

previous_value = 0
for x in c:

    for y in c:
        if(2020 == x+y):
            print ("Found it !")
            print (x)
            print (y)
            print ("The product is:")
            print (x*y)

    
# the result:    
# Found it !
# 118.0
# 1902.0
# The product is:
# 224436.0





# Fail #01
# 
# The following code works, however I got the following error message:
#   "Puzzle inputs differ by user.Please log in to get your puzzle input."   
# import requests
# link = 'https://adventofcode.com/2020/day/1/input'
#f = requests.get(link)
# print(f.text)









"""
For information: this is the puzzle input:

2010
1856
1905
1786
1557
1995
1830
1971
1909
1500
1806
1846
2003
1839
1943
1977
1537
689
1861
1886
1815
1763
1834
1881
1952
1853
1775
1835
1874
1948
1978
347
1672
885
1709
1826
1911
1644
1064
1561
1966
1352
1347
1928
1756
615
1513
1932
1968
1762
1842
1475
1921
1716
1533
1975
1924
1850
1456
1783
1587
1913
1908
1502
1993
1635
1691
1706
1871
1857
1915
1604
1618
1902
1860
1648
1933
1999
1960
1389
1858
1793
1609
1484
1735
1535
1891
1879
1517
1766
1926
1668
1495
1585
1831
1308
1767
1479
1638
1600
710
1685
1818
1859
1822
1844
1550
1872
1719
1863
1987
199
1840
1817
1752
1612
1983
1838
1504
1997
716
1862
1931
1356
1645
1962
1574
1914
1869
1919
1487
1961
1728
1867
1177
1757
1316
1875
1991
1646
700
1972
2004
1577
118
1954
1483
1516
2007
1506
1588
1698
1725
2006
179
1849
1894
1695
1399
1726
1658
1920
1825
1837
1878
1591
1611
1409
1553
1705
1845
1718
1732
1639
1885
1929
1887
1787
1541
1946
1391
1884
1938
1496
1720
1669
1965
1967
1890
1743
1889
1970
1866
1912
1785
1998
1708
1810
1939
2005

"""



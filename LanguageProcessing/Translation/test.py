
from LanguageProcessing.Translation.GoogleTranslator import  GoogleTranslator



translator = GoogleTranslator(destination_language='uk')
result = translator.get_translation(u"""
In the west, M-28 begins at a signalized intersection with US 2 in Wakefield. Heading north, the highway passes Sunday Lake heading out of town. After crossing into southwestern Ontonagon County and the Eastern Time Zone, the trunkline highway skirts the northern shore of Lake Gogebic, running concurrently with M-64. The first section of M-28 designated as a part of the Lake Superior Circle Tour is from the western terminus to the eastern junction with M-64 in Bergland, where the Circle Tour turns north along M-64, leaving M-28. Here, M-28 has its lowest traffic counts; within the 2013 MDOT survey, the road is listed with only an average annual daily traffic (AADT) of 1,425 vehicles on a section of highway between Bergland and the US 45 intersection in Bruce Crossing.[6] The trunkline runs through heavily forested areas of southern Houghton and Baraga counties. At the eastern junction with US 41 near Covington, M-28 receives the Circle Tour designation again[4] and exits the Ottawa National Forest.[7]

In Baraga and Marquette counties, US 41/M-28 passes through hilly terrain before entering the urban areas of Ishpeming, Negaunee and Marquette.[3] Approximately 13,000–17,000 vehicles use this section from Ishpeming eastward through Negaunee. West of the city of Marquette, US 41/M-28 had a peak 2013 AADT of 32,805 vehicles in Marquette Township along a retail and business corridor. This peak level is sustained until the start of the Marquette Bypass, where the traffic returns to the 16,500-vehicle and higher levels seen in Ishpeming and Negaunee. South of the city of Marquette, traffic counts once again climb to 19,620 vehicles. In Chocolay Township the AADT drops to 8,840 vehicles before tapering off to 3,065 vehicles by the county line.[6]

At the Ishpeming–Negaunee city line, M-28 changes memorial highway designations. From the western terminus to this point, M-28 is called the "Veterans Memorial Highway", but it becomes the "D. J. Jacobetti Memorial Highway" to honor the longest-serving member of the Michigan Legislature, Dominic J. Jacobetti.[8][9] The Jacobetti Highway designation ends at the eastern M-123 junction in Chippewa County.[10]

A brown and white wooden sign for the Hiawatha National Forest mounted on a stone base. The sign is installed on the right side of a highway between the road and the forest on the far right.
Hiawatha National Forest road sign on M-28/M-94 in Alger County west of Shingleton
Between Marquette and Munising, M-28 closely parallels the Lake Superior shoreline, providing scenic views of the lake and its "lonesome sandy beaches".[11][12] The Lakenenland Sculpture Park is located in Chocolay Township near Shot Point in eastern Marquette County. This roadside attraction is owned by Tom Lakenen and features fanciful works of art made of scrap iron.[13] Near the community of Au Train, M-28 crosses into the western unit of the Hiawatha National Forest.[7] West of Munising is a ferry dock offering transport to the Grand Island National Recreation Area, and at Munising there is easy access to Pictured Rocks National Lakeshore. The roadway also features variable-message signs to warn motorists of winter weather-related traffic closures along the lakeshore. Installed at the US 41 and M-94 junctions, the signs advise motorists which sections of roadway are closed. Per MDOT policy, only snowplows are allowed on these sections during a closure.[14] The highway exits the Hiawatha National Forest at the Alger County–Schoolcraft County line along the Seney Stretch.
""", max_symbols_count=4000)
print(result['translation'])


print('\n\n\n')

translator = GoogleTranslator()
result = translator.get_translation(u"""
للغه العربى (اللغة العربية) هى لغه ساميه مركزيه, و بكده تصنيفها بيكون مع اللغات الساميه التانيه زى العبرى والأرامى. العربى القياسى الحديث هو اللى بيتدرس فى المدارس والجامعات, و بيستعمل فى اماكن الشغل و الحكومه و معظم وسايل الإعلام (ميديا).[1] كود اللغه بالنسبه لقانون المنظمه الدوليه للتوحيد القياسى (ايزو 639) (ISO 639), هو ar
اللهجة السايده فى كل بلد لغته الرسمى عربى مختلفه. مثلا فى مصر مع ان اللغه الرسمى عربى, معظم سكّانها بيتكلّمو اللغه المصريه الحديثه,[1] و هى لغه معترف بيها فى العالم عن طريق كود اللغه بالنسبه لقانون المنظمه الدوليه للتوحيد القياسى (ايزو 639) (ISO 639), و هو arz. فيه مصادر بتقول ان انواع اللغه العربى (انجليزى: varieties of Arabic; مش اللغه العربى الكلاسيكى او القياسيه الحديثه) بيستعملها 206 مليون شخص كلغتهم الاولانيه و 248 مليون شخص غيرهم
""", max_symbols_count=4000)
print(result['translation'])



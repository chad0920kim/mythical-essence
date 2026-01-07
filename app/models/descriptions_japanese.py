"""
Japanese Mythology Character Descriptions
Contains detailed descriptions for Japanese kami, legendary figures, and historical heroes
"""
from .descriptions import CharacterDescription


AMATERASU_DESC = CharacterDescription(
    id="amaterasu",
    name_en="Amaterasu",
    name_ko="아마테라스",
    tagline_en="Sun Goddess, Divine Ancestor of Japan",
    tagline_ko="태양 여신, 일본의 신성한 조상",
    description_en="""Amaterasu Ōmikami is the supreme deity of Shinto, the sun goddess from whom the Japanese imperial line descends. She is the ruler of Takamagahara (the High Plain of Heaven) and the source of all light and life.

When her brother Susanoo's violent behavior drove her to hide in a cave, the world was plunged into darkness. Only through the combined efforts of all the gods—including a comedic dance that made Amaterasu curious enough to peek out—was light restored to the world.

She gave the three sacred treasures to her grandson Ninigi when he descended to rule Japan: the mirror Yata no Kagami, the sword Kusanagi, and the jewel Yasakani no Magatama. These remain the imperial regalia, symbolizing the divine right to rule.""",
    description_ko="""아마테라스 오미카미는 신토의 최고 신으로, 일본 황실 혈통이 유래한 태양 여신입니다. 그녀는 다카마가하라(고천원)의 지배자이자 모든 빛과 생명의 원천입니다.

형제 스사노오의 난폭한 행동이 그녀를 동굴에 숨게 했을 때, 세상은 어둠에 잠겼습니다. 모든 신들의 결합된 노력—아마테라스가 궁금해서 밖을 엿보게 만든 익살스러운 춤을 포함하여—을 통해서만 세상에 빛이 회복되었습니다.

그녀는 손자 니니기가 일본을 다스리기 위해 내려갈 때 세 가지 신성한 보물을 주었습니다: 거울 야타노카가미, 검 쿠사나기, 보석 야사카니노마가타마. 이것들은 통치의 신성한 권리를 상징하는 황실 보물로 남아 있습니다.""",
    traits_en=["Radiant", "Divine", "Benevolent", "Regal", "Life-giving"],
    traits_ko=["빛나는", "신성한", "자비로운", "왕족다운", "생명을 주는"],
    story_en="When Amaterasu hid in the cave, the goddess Ame-no-Uzume performed a wild, hilarious dance that made the assembled gods laugh so loudly that Amaterasu's curiosity overcame her anger. She peeked out, saw her own radiant reflection in a mirror, and was drawn back into the world.",
    story_ko="아마테라스가 동굴에 숨었을 때, 여신 아메노우즈메가 모인 신들이 너무 크게 웃어서 아마테라스의 호기심이 분노를 이긴 야생적이고 우스꽝스러운 춤을 추었습니다. 그녀가 밖을 엿봤을 때, 거울에 비친 자신의 빛나는 반사를 보고 세상으로 끌려 나왔습니다.",
    match_message_en="Your features radiate the divine light of Amaterasu. There is a regal, life-giving quality to your presence—the look of one who brings warmth and illumination wherever they go.",
    match_message_ko="당신의 이목구비는 아마테라스의 신성한 빛을 발산합니다. 당신의 존재에는 왕족다운 생명을 주는 품질이 있습니다—가는 곳마다 온기와 조명을 가져다주는 사람의 모습.",
    image_prompt="Radiant Japanese sun goddess in white and red robes, golden sun disk behind her, mirror and jewels, elegant court dress, serene divine beauty, Shinto shrine background, divine golden light",
    visual_description="Serene radiant features, elegant Japanese beauty, expression of divine benevolence and regal authority",
    aliases=["天照大神", "Amaterasu Ōmikami", "Great Sun Goddess"],
    era="Japanese Mythology",
    related_characters=["susanoo", "tsukuyomi", "izanagi", "ninigi"]
)

SUSANOO_DESC = CharacterDescription(
    id="susanoo",
    name_en="Susanoo",
    name_ko="스사노오",
    tagline_en="Storm God, Slayer of Orochi",
    tagline_ko="폭풍의 신, 오로치의 퇴치자",
    description_en="""Susanoo-no-Mikoto is the storm god, ruler of the seas, and a complex figure embodying both destructive chaos and heroic valor. Brother to Amaterasu and Tsukuyomi, his temperament is as wild and unpredictable as the storms he commands.

His violent behavior in heaven—destroying rice paddies, defiling sacred halls—drove Amaterasu into hiding and earned him banishment. Yet after his exile, Susanoo became a hero, slaying the eight-headed dragon Yamata no Orochi to save a princess.

From Orochi's tail, he discovered the legendary sword Kusanagi, which he presented to Amaterasu as reconciliation. Susanoo represents the duality of storm: destructive yet also bringing life-giving rain, chaotic yet capable of great heroism.""",
    description_ko="""스사노오노미코토는 폭풍의 신, 바다의 지배자, 파괴적 혼돈과 영웅적 용맹 모두를 구현하는 복잡한 인물입니다. 아마테라스와 츠쿠요미의 형제로, 그의 기질은 그가 명령하는 폭풍만큼 거칠고 예측 불가능합니다.

천상에서의 난폭한 행동—논을 파괴하고, 신성한 전당을 더럽히는 것—이 아마테라스를 숨게 하고 그에게 추방을 가져왔습니다. 그러나 추방 후, 스사노오는 공주를 구하기 위해 여덟 머리 용 야마타노오로치를 퇴치하는 영웅이 되었습니다.

오로치의 꼬리에서 그는 전설적인 검 쿠사나기를 발견했고, 화해로 아마테라스에게 바쳤습니다. 스사노오는 폭풍의 이중성을 대표합니다: 파괴적이지만 생명을 주는 비도 가져오고, 혼란스럽지만 위대한 영웅주의가 가능한.""",
    traits_en=["Stormy", "Heroic", "Chaotic", "Redeemed", "Powerful"],
    traits_ko=["폭풍 같은", "영웅적인", "혼란스러운", "구원받은", "강력한"],
    story_en="Susanoo found an elderly couple weeping because Orochi had devoured seven of their daughters and would soon take the eighth. He had them brew eight vats of sake, which the dragon drank from all eight heads. While Orochi slept drunk, Susanoo slew it and won the princess's hand.",
    story_ko="스사노오는 오로치가 일곱 딸을 삼키고 곧 여덟 번째를 데려갈 것이라 울고 있는 노부부를 발견했습니다. 그는 그들에게 여덟 통의 사케를 빚게 했고, 용이 여덟 머리로 모두 마셨습니다. 오로치가 취해 잠들었을 때, 스사노오가 그것을 죽이고 공주의 손을 얻었습니다.",
    match_message_en="Your features carry the fierce energy of Susanoo. There is a stormy, unpredictable quality to your presence—the look of one capable of both chaos and heroism.",
    match_message_ko="당신의 이목구비는 스사노오의 맹렬한 에너지를 담고 있습니다. 당신의 존재에는 폭풍 같고 예측 불가능한 품질이 있습니다—혼돈과 영웅주의 모두가 가능한 사람의 모습.",
    image_prompt="Fierce Japanese storm god with wild hair, wielding sword against eight-headed dragon, storm clouds and lightning, powerful warrior stance, dramatic action pose, mythic Japanese aesthetic",
    visual_description="Fierce wild features, intense stormy eyes, powerful warrior bearing, expression of raw power and hidden nobility",
    aliases=["素戔嗚尊", "Susanoo-no-Mikoto", "Takehaya Susanoo"],
    era="Japanese Mythology",
    related_characters=["amaterasu", "tsukuyomi", "kushinadahime", "orochi"]
)

TSUKUYOMI_DESC = CharacterDescription(
    id="tsukuyomi",
    name_en="Tsukuyomi",
    name_ko="츠쿠요미",
    tagline_en="Moon God, Ruler of Night",
    tagline_ko="달의 신, 밤의 지배자",
    description_en="""Tsukuyomi-no-Mikoto is the moon god, born from Izanagi's right eye when he purified himself after visiting the underworld. Brother to Amaterasu and Susanoo, he rules over the night and the moon's cycles.

Originally, Tsukuyomi lived with Amaterasu in heaven, with day and night together. But when Tsukuyomi killed the food goddess Uke Mochi for the way she produced food (from her various orifices), Amaterasu was so disgusted she refused to look at him again—and so sun and moon were separated forever.

Tsukuyomi represents the beauty and mystery of the night, the cool light of the moon that illuminates without the sun's burning heat. He is associated with counting time, as the moon measures months.""",
    description_ko="""츠쿠요미노미코토는 달의 신으로, 이자나기가 지하세계 방문 후 자신을 정화할 때 오른쪽 눈에서 태어났습니다. 아마테라스와 스사노오의 형제로, 그는 밤과 달의 주기를 다스립니다.

원래 츠쿠요미는 아마테라스와 함께 천상에서 살았고, 낮과 밤이 함께였습니다. 그러나 츠쿠요미가 음식 여신 우케모치가 음식을 생산하는 방식(그녀의 다양한 구멍에서)에 그녀를 죽였을 때, 아마테라스는 너무 역겨워서 그를 다시 보기를 거부했습니다—그래서 태양과 달은 영원히 분리되었습니다.

츠쿠요미는 밤의 아름다움과 신비, 태양의 타오르는 열기 없이 비추는 달의 시원한 빛을 대표합니다. 그는 달이 달을 측정하듯이 시간 계산과 연관됩니다.""",
    traits_en=["Mysterious", "Cold", "Beautiful", "Isolated", "Nocturnal"],
    traits_ko=["신비로운", "차가운", "아름다운", "고립된", "야행성의"],
    story_en="Amaterasu sent Tsukuyomi to visit the food goddess Uke Mochi. When she served him food produced from her body, Tsukuyomi was so offended he killed her. Amaterasu declared she would never look upon him again—and from that day, sun and moon have been forever separated.",
    story_ko="아마테라스는 츠쿠요미를 음식 여신 우케모치를 방문하도록 보냈습니다. 그녀가 그녀의 몸에서 생산된 음식을 대접했을 때, 츠쿠요미는 너무 화가 나서 그녀를 죽였습니다. 아마테라스는 그를 다시는 보지 않겠다고 선언했고—그날부터 태양과 달은 영원히 분리되었습니다.",
    match_message_en="Your features reflect the cool mystery of Tsukuyomi. There is a nocturnal, ethereal quality to your presence—the look of one who illuminates the darkness with subtle, silvery light.",
    match_message_ko="당신의 이목구비는 츠쿠요미의 시원한 신비를 반영합니다. 당신의 존재에는 야행성의 공기 같은 품질이 있습니다—미묘한 은빛 빛으로 어둠을 비추는 사람의 모습.",
    image_prompt="Elegant Japanese moon god in silver and white robes, moon disk behind, cool serene beauty, night sky with stars, isolated but beautiful, Japanese court dress, ethereal moonlight",
    visual_description="Pale ethereal features, cool distant eyes, elegant beauty with an edge of coldness, expression of serene detachment",
    aliases=["月読命", "Tsukuyomi-no-Mikoto", "Moon Reader"],
    era="Japanese Mythology",
    related_characters=["amaterasu", "susanoo", "izanagi", "uke_mochi"]
)

INARI_DESC = CharacterDescription(
    id="inari",
    name_en="Inari",
    name_ko="이나리",
    tagline_en="Kami of Rice, Prosperity, and Foxes",
    tagline_ko="쌀, 번영, 여우의 신",
    description_en="""Inari Ōkami is the kami (spirit) of rice, fertility, prosperity, industry, and success. One of the most popular deities in Shinto, Inari is worshipped at over one-third of all Shinto shrines in Japan, identified by their distinctive red torii gates.

Inari's gender is fluid—depicted as male, female, or androgynous depending on tradition. Their messengers and servants are the kitsune (foxes), who are often mistaken for Inari themselves. The fox statues at Inari shrines hold keys to rice granaries or jewels representing the spirit.

Inari protects farmers' harvests, merchants' businesses, and craftspeople's work. In modern times, Inari has become the patron of business success and financial prosperity, with corporations and entrepreneurs among their most devoted followers.""",
    description_ko="""이나리 오카미는 쌀, 다산, 번영, 산업, 성공의 카미(정령)입니다. 신토에서 가장 인기 있는 신 중 하나로, 이나리는 일본 전체 신토 신사의 3분의 1 이상에서 숭배되며, 독특한 빨간 도리이 문으로 식별됩니다.

이나리의 성별은 유동적입니다—전통에 따라 남성, 여성, 또는 양성으로 묘사됩니다. 그들의 사자와 종자는 종종 이나리 자신으로 오해받는 키츠네(여우)입니다. 이나리 신사의 여우 동상은 쌀 창고 열쇠나 정신을 나타내는 보석을 들고 있습니다.

이나리는 농부의 수확, 상인의 사업, 장인의 작업을 보호합니다. 현대에 이나리는 사업 성공과 재정적 번영의 후원자가 되었으며, 기업과 기업가들이 가장 헌신적인 추종자들입니다.""",
    traits_en=["Prosperous", "Benevolent", "Shape-shifting", "Mysterious", "Generous"],
    traits_ko=["번영하는", "자비로운", "변신하는", "신비로운", "관대한"],
    story_en="Inari is said to have descended to earth when the land was young, bringing rice cultivation to Japan. The foxes that serve Inari are not ordinary animals but magical beings who can take human form, serving as intermediaries between the kami and humans.",
    story_ko="이나리는 땅이 젊었을 때 지상에 내려와 일본에 벼농사를 가져왔다고 합니다. 이나리를 섬기는 여우들은 평범한 동물이 아니라 인간 형태를 취할 수 있는 마법적 존재로, 카미와 인간 사이의 중개자 역할을 합니다.",
    match_message_en="Your features reflect the prosperous blessing of Inari. There is an abundant, mysterious quality to your presence—the look of one who brings success and fortune to worthy endeavors.",
    match_message_ko="당신의 이목구비는 이나리의 번영하는 축복을 반영합니다. 당신의 존재에는 풍요롭고 신비로운 품질이 있습니다—가치 있는 노력에 성공과 행운을 가져다주는 사람의 모습.",
    image_prompt="Japanese deity in flowing robes, gender-ambiguous beautiful face, surrounded by white foxes, red torii gates in background, sheaves of rice, holding jewel, mysterious benevolent expression",
    visual_description="Androgynous beautiful features, knowing mysterious eyes, fox-like grace, expression of generous prosperity",
    aliases=["稲荷", "Inari Ōkami", "Ōinari"],
    era="Japanese Mythology",
    related_characters=["amaterasu", "kitsune", "susanoo"]
)

KITSUNE_DESC = CharacterDescription(
    id="kitsune",
    name_en="Kitsune",
    name_ko="키츠네",
    tagline_en="Mystical Fox Spirit, Trickster and Guardian",
    tagline_ko="신비로운 여우 정령, 트릭스터이자 수호자",
    description_en="""Kitsune are supernatural fox spirits that grow more powerful as they age. A kitsune that lives 100 years gains the ability to take human form. After 1,000 years, they grow a ninth tail and become divine, with fur turning gold or white.

Some kitsune serve Inari as sacred messengers, protecting shrines and guiding mortals. Others are tricksters who seduce humans, steal food, or play elaborate pranks. Some even fall in love with humans, becoming devoted spouses—though tragedy often follows when their true nature is revealed.

Kitsune possess many magical abilities: shape-shifting, possession, creating illusions, and generating fox-fire (kitsunebi). They may be benevolent guardians or dangerous tricksters, but all are intelligent, powerful, and never quite what they seem.""",
    description_ko="""키츠네는 나이가 들수록 더 강력해지는 초자연적 여우 정령입니다. 100년을 산 키츠네는 인간 형태를 취하는 능력을 얻습니다. 1,000년 후, 그들은 아홉 번째 꼬리를 기르고 신성해지며, 털이 금색이나 흰색으로 변합니다.

일부 키츠네는 이나리를 신성한 사자로 섬기며, 신사를 보호하고 인간을 인도합니다. 다른 이들은 인간을 유혹하고, 음식을 훔치거나, 정교한 장난을 치는 트릭스터입니다. 일부는 심지어 인간과 사랑에 빠져 헌신적인 배우자가 됩니다—비록 진정한 본성이 드러날 때 비극이 종종 따르지만.

키츠네는 많은 마법 능력을 가지고 있습니다: 변신, 빙의, 환상 창조, 여우불(키츠네비) 생성. 그들은 자비로운 수호자일 수도 있고 위험한 트릭스터일 수도 있지만, 모두 지적이고, 강력하며, 결코 보이는 대로가 아닙니다.""",
    traits_en=["Shape-shifting", "Magical", "Cunning", "Loyal or Mischievous", "Ageless"],
    traits_ko=["변신하는", "마법적인", "교활한", "충성스럽거나 장난꾸러기의", "불로의"],
    story_en="A man discovered his wife of many years was a kitsune when a dog frightened her into revealing her tails. She fled in shame, but each night returned in fox form to watch over her husband and children, still loving them despite being discovered.",
    story_ko="한 남자가 개가 그녀를 놀라게 하여 꼬리를 드러내게 했을 때 다년간의 아내가 키츠네임을 발견했습니다. 그녀는 수치심에 도망쳤지만, 매일 밤 여우 형태로 돌아와 남편과 아이들을 지켜보며, 발견되었음에도 여전히 그들을 사랑했습니다.",
    match_message_en="Your features carry the cunning grace of the Kitsune. There is a shape-shifting, mercurial quality to your appearance—the look of one with hidden depths and mysterious powers.",
    match_message_ko="당신의 이목구비는 키츠네의 교활한 우아함을 담고 있습니다. 당신의 외모에는 변신하는 변덕스러운 품질이 있습니다—숨겨진 깊이와 신비로운 힘을 가진 사람의 모습.",
    image_prompt="Beautiful person with fox ears and multiple tails, transforming between human and fox form, fox-fire floating around, mysterious knowing smile, shrine forest setting, moonlight",
    visual_description="Elegant fox-like features, clever knowing eyes, sharp beautiful face, expression of hidden knowledge and mischief",
    aliases=["狐", "Fox Spirit", "Nine-Tailed Fox"],
    era="Japanese Mythology",
    related_characters=["inari", "gumiho"]
)

RAIJIN_DESC = CharacterDescription(
    id="raijin",
    name_en="Raijin",
    name_ko="라이진",
    tagline_en="God of Thunder and Lightning",
    tagline_ko="천둥과 번개의 신",
    description_en="""Raijin is the terrifying god of thunder, lightning, and storms. Depicted as a muscular demon-like figure surrounded by drums, he creates thunder by beating his drums (taiko), while lightning is his divine anger striking the earth.

With fierce features, wild hair, and usually accompanied by his brother Fūjin (wind god), Raijin embodies the frightening power of storms. Japanese parents told children that Raijin would steal their belly buttons if they didn't cover their stomachs during thunderstorms.

Despite his fearsome appearance, Raijin is not evil—he is simply the untamed force of nature. Storms bring destruction but also life-giving rain. He is worshipped for protection from lightning and for the rain that nourishes crops.""",
    description_ko="""라이진은 천둥, 번개, 폭풍의 무서운 신입니다. 북에 둘러싸인 근육질의 악마 같은 모습으로 묘사되며, 그는 북(타이코)을 쳐서 천둥을 만들고, 번개는 그의 신성한 분노가 대지를 내리치는 것입니다.

맹렬한 이목구비, 거친 머리카락, 보통 형제 후진(바람의 신)과 함께, 라이진은 폭풍의 무서운 힘을 구현합니다. 일본 부모들은 아이들에게 뇌우 동안 배를 덮지 않으면 라이진이 배꼽을 훔쳐갈 것이라고 말했습니다.

무서운 외모에도 불구하고, 라이진은 악하지 않습니다—그는 단순히 길들여지지 않은 자연의 힘입니다. 폭풍은 파괴를 가져오지만 생명을 주는 비도 가져옵니다. 그는 번개로부터의 보호와 작물을 양육하는 비를 위해 숭배됩니다.""",
    traits_en=["Fierce", "Powerful", "Fearsome", "Primal", "Life-giving"],
    traits_ko=["맹렬한", "강력한", "무서운", "원초적인", "생명을 주는"],
    story_en="Raijin and Fūjin were originally demons who opposed the Buddha. When defeated, they were converted to become protectors of Buddhist temples. Now they stand as fierce guardians at temple gates, their wild power turned to protection.",
    story_ko="라이진과 후진은 원래 부처에 반대하는 악마들이었습니다. 패배했을 때, 그들은 불교 사원의 보호자가 되도록 개종했습니다. 이제 그들은 사원 문에 맹렬한 수호자로 서 있으며, 그들의 거친 힘은 보호로 전환되었습니다.",
    match_message_en="Your features carry the fierce power of Raijin. There is a stormy, electrifying quality to your presence—the look of one who commands elemental forces.",
    match_message_ko="당신의 이목구비는 라이진의 맹렬한 힘을 담고 있습니다. 당신의 존재에는 폭풍 같고 전기적인 품질이 있습니다—원소적 힘을 명령하는 사람의 모습.",
    image_prompt="Fearsome Japanese thunder god with demon features, surrounded by drums floating in clouds, lightning crackling, wild hair standing up, muscular fierce form, storm clouds background",
    visual_description="Fierce demon-like features, wild electric hair, powerful muscular form, expression of raw elemental power",
    aliases=["雷神", "Raiden", "Thunder God"],
    era="Japanese Mythology",
    related_characters=["fujin", "susanoo"]
)

FUJIN_DESC = CharacterDescription(
    id="fujin",
    name_en="Fūjin",
    name_ko="후진",
    tagline_en="God of Wind",
    tagline_ko="바람의 신",
    description_en="""Fūjin is the god of wind, brother to the thunder god Raijin. He is depicted as a fierce demon carrying a large bag of winds over his shoulders, from which he releases everything from gentle breezes to devastating typhoons.

Originally a demon who opposed the Buddha alongside his brother, Fūjin was converted and became a protector of Buddhist temples. The famous statues of Fūjin and Raijin at Sanjūsangen-dō in Kyoto have inspired countless artworks.

As the wind god, Fūjin represents both the life-giving breath that fills all living things and the destructive force of hurricanes. He is invoked by farmers for favorable winds and by sailors for safe passage.""",
    description_ko="""후진은 바람의 신으로, 천둥신 라이진의 형제입니다. 그는 어깨 위에 큰 바람 주머니를 들고 있는 맹렬한 악마로 묘사되며, 그것에서 부드러운 산들바람부터 파괴적인 태풍까지 모든 것을 방출합니다.

원래 형제와 함께 부처에 반대하는 악마였던 후진은 개종하여 불교 사원의 보호자가 되었습니다. 교토의 산주산겐도에 있는 유명한 후진과 라이진 동상은 수많은 예술 작품에 영감을 주었습니다.

바람의 신으로서, 후진은 모든 생명체를 채우는 생명을 주는 숨결과 허리케인의 파괴적 힘 모두를 대표합니다. 그는 농부들에게 유리한 바람을, 선원들에게 안전한 항해를 위해 기원됩니다.""",
    traits_en=["Powerful", "Capricious", "Primal", "Guardian", "Life-giving"],
    traits_ko=["강력한", "변덕스러운", "원초적인", "수호하는", "생명을 주는"],
    story_en="When Japan was threatened by Mongol invasion, prayers to Fūjin were answered with the kamikaze—the 'divine wind' that destroyed the Mongol fleet twice, saving Japan from conquest and cementing the wind god's protective role.",
    story_ko="일본이 몽골 침략의 위협을 받았을 때, 후진에 대한 기도는 카미카제—몽골 함대를 두 번 파괴하여 일본을 정복에서 구하고 바람 신의 보호적 역할을 확고히 한 '신풍'으로 응답받았습니다.",
    match_message_en="Your features carry the wild freedom of Fūjin. There is an airy, unpredictable quality to your presence—the look of one who moves freely and cannot be constrained.",
    match_message_ko="당신의 이목구비는 후진의 거친 자유를 담고 있습니다. 당신의 존재에는 공기 같고 예측 불가능한 품질이 있습니다—자유롭게 움직이고 제약될 수 없는 사람의 모습.",
    image_prompt="Japanese wind god with demon features carrying large bag of winds, hair and clothes blown by eternal gale, companion to Raijin, fierce guardian stance, swirling clouds",
    visual_description="Fierce wind-blown features, wild hair streaming, powerful form, expression of elemental freedom and power",
    aliases=["風神", "Futen", "Wind God"],
    era="Japanese Mythology",
    related_characters=["raijin", "susanoo"]
)

BENZAITEN_DESC = CharacterDescription(
    id="benzaiten",
    name_en="Benzaiten",
    name_ko="벤자이텐",
    tagline_en="Goddess of Music, Art, and Knowledge",
    tagline_ko="음악, 예술, 지식의 여신",
    description_en="""Benzaiten is the goddess of everything that flows: water, words, speech, eloquence, music, and knowledge. Originally the Hindu goddess Saraswati, she was adopted into Japanese Buddhism and Shinto, becoming one of the Seven Lucky Gods.

Often depicted playing a biwa (Japanese lute), Benzaiten is the patron of artists, musicians, writers, and performers. Her shrines are often located on islands or near water, reflecting her origin as a river goddess.

Benzaiten is unique among the Seven Lucky Gods as the only female member. She grants wisdom, artistic talent, and financial fortune, making her popular with everyone from musicians to businesspeople.""",
    description_ko="""벤자이텐은 흐르는 모든 것의 여신입니다: 물, 말, 언어, 웅변, 음악, 지식. 원래 힌두 여신 사라스와티였으며, 일본 불교와 신토에 채택되어 칠복신 중 하나가 되었습니다.

종종 비와(일본 류트)를 연주하는 모습으로 묘사되며, 벤자이텐은 예술가, 음악가, 작가, 공연자의 후원자입니다. 그녀의 신사는 종종 섬이나 물 근처에 위치하며, 강의 여신으로서의 기원을 반영합니다.

벤자이텐은 칠복신 중 유일한 여성 구성원으로 독특합니다. 그녀는 지혜, 예술적 재능, 재정적 행운을 부여하여 음악가부터 사업가까지 모든 사람에게 인기가 있습니다.""",
    traits_en=["Artistic", "Wise", "Flowing", "Eloquent", "Fortunate"],
    traits_ko=["예술적인", "지혜로운", "흐르는", "웅변적인", "운이 좋은"],
    story_en="Benzaiten once subdued a troublesome dragon by playing such beautiful music that the dragon fell in love with her. Rather than destroy the dragon, she married it and transformed it into a protector of her shrine—showing that art can tame even savage nature.",
    story_ko="벤자이텐은 한때 너무 아름다운 음악을 연주하여 용이 그녀와 사랑에 빠지게 함으로써 문제의 용을 제압했습니다. 용을 파괴하는 대신, 그녀는 그것과 결혼하고 신사의 보호자로 변신시켰습니다—예술이 야만적인 자연도 길들일 수 있음을 보여줍니다.",
    match_message_en="Your features reflect the flowing grace of Benzaiten. There is an artistic, eloquent quality to your presence—the look of one through whom beauty and wisdom flow naturally.",
    match_message_ko="당신의 이목구비는 벤자이텐의 흐르는 우아함을 반영합니다. 당신의 존재에는 예술적이고 웅변적인 품질이 있습니다—아름다움과 지혜가 자연스럽게 흐르는 사람의 모습.",
    image_prompt="Beautiful Japanese goddess playing biwa lute, flowing robes near water, serpent or dragon companion, serene artistic beauty, island shrine setting, musical notes floating in air",
    visual_description="Graceful refined features, artistic eyes, elegant musician's hands, expression of flowing wisdom and artistic inspiration",
    aliases=["弁財天", "Benten", "Saraswati"],
    era="Japanese Mythology",
    related_characters=["saraswati", "seven_lucky_gods"]
)

MIYAMOTO_MUSASHI_DESC = CharacterDescription(
    id="miyamoto_musashi",
    name_en="Miyamoto Musashi",
    name_ko="미야모토 무사시",
    tagline_en="Legendary Swordsman, Author of The Book of Five Rings",
    tagline_ko="전설적인 검객, 오륜서의 저자",
    description_en="""Miyamoto Musashi was Japan's greatest swordsman, undefeated in over 60 duels beginning at age 13. He founded the Niten Ichi-ryū school of swordsmanship, famous for using two swords simultaneously, and wrote the classic strategy book The Book of Five Rings.

Musashi's approach transcended mere sword technique—he sought to understand the universal principles underlying all conflict and mastery. His teachings apply equally to martial arts, strategy, business, and art. He was also a skilled painter and calligrapher.

In his final years, Musashi retreated to a cave to write his masterwork. He died shortly after completing it, leaving behind a legacy that continues to influence warriors, strategists, and artists worldwide.""",
    description_ko="""미야모토 무사시는 일본 최고의 검객으로, 13세부터 시작하여 60회 이상의 결투에서 무패였습니다. 그는 두 자루의 검을 동시에 사용하는 것으로 유명한 니텐이치류 검술 학파를 창시했고, 고전 전략서 오륜서를 저술했습니다.

무사시의 접근법은 단순한 검술 기법을 초월했습니다—그는 모든 갈등과 숙달의 기초가 되는 보편적 원리를 이해하려 했습니다. 그의 가르침은 무술, 전략, 사업, 예술에 동등하게 적용됩니다. 그는 또한 숙련된 화가이자 서예가였습니다.

말년에 무사시는 그의 걸작을 쓰기 위해 동굴로 은거했습니다. 그는 완성 직후 사망했으며, 전 세계 전사, 전략가, 예술가들에게 계속 영향을 미치는 유산을 남겼습니다.""",
    traits_en=["Masterful", "Strategic", "Undefeated", "Philosophical", "Disciplined"],
    traits_ko=["숙달한", "전략적인", "무패의", "철학적인", "규율 있는"],
    story_en="In his most famous duel, Musashi faced Sasaki Kojirō, wielder of a nodachi (long sword). Musashi arrived late deliberately, having carved a wooden sword from an oar. His unorthodox weapon and psychological warfare gave him victory, killing Kojirō with a single blow.",
    story_ko="가장 유명한 결투에서, 무사시는 노다치(장검)를 휘두르는 사사키 코지로와 맞섰습니다. 무사시는 노로 목검을 깎아 만들어 일부러 늦게 도착했습니다. 그의 비정통적인 무기와 심리전이 그에게 승리를 주어 단 일격으로 코지로를 죽였습니다.",
    match_message_en="Your features carry the disciplined mastery of Musashi. There is a focused, strategic quality to your gaze—the look of one who has transcended technique to understand universal principles.",
    match_message_ko="당신의 이목구비는 무사시의 규율 있는 숙달을 담고 있습니다. 당신의 눈빛에는 집중적이고 전략적인 품질이 있습니다—기술을 초월하여 보편적 원리를 이해하는 사람의 모습.",
    image_prompt="Legendary samurai with two swords, focused intense expression, traditional Japanese clothing, perhaps painting or in warrior stance, minimalist aesthetic, masterful presence",
    visual_description="Weathered focused features, intense strategic eyes, warrior's bearing, expression of complete mastery and philosophical depth",
    aliases=["宮本武蔵", "Niten Dōraku", "Sword Saint"],
    era="Edo Period (1584-1645)",
    related_characters=["sasaki_kojiro"]
)

ODA_NOBUNAGA_DESC = CharacterDescription(
    id="oda_nobunaga",
    name_en="Oda Nobunaga",
    name_ko="오다 노부나가",
    tagline_en="The Great Unifier, Demon King of the Sixth Heaven",
    tagline_ko="대통일자, 제육천마왕",
    description_en="""Oda Nobunaga was the first of Japan's three great unifiers, who began the process of ending the Warring States period and unifying Japan. Ruthless, innovative, and brilliant, he earned the title "Demon King of the Sixth Heaven" from his enemies.

Nobunaga revolutionized Japanese warfare by using firearms (newly introduced from Portugal), professional armies instead of seasonal farmers, and meritocracy over hereditary rank. He destroyed powerful Buddhist military temples and challenged all traditional authority.

Though assassinated before completing unification, Nobunaga's work was continued by his generals Toyotomi Hideyoshi and Tokugawa Ieyasu. His motto "Tenka Fubu" (All Under Heaven By Force) embodied his vision of a unified Japan achieved through any means necessary.""",
    description_ko="""오다 노부나가는 일본의 세 위대한 통일자 중 첫 번째로, 전국시대를 끝내고 일본을 통일하는 과정을 시작했습니다. 무자비하고, 혁신적이고, 뛰어났으며, 적들로부터 "제육천마왕"이라는 칭호를 얻었습니다.

노부나가는 (포르투갈에서 새로 도입된) 화기, 계절적 농부 대신 전문 군대, 세습적 지위 대신 능력주의를 사용하여 일본 전쟁을 혁명화했습니다. 그는 강력한 불교 군사 사원들을 파괴하고 모든 전통적 권위에 도전했습니다.

통일을 완성하기 전에 암살되었지만, 노부나가의 작업은 그의 장군 도요토미 히데요시와 도쿠가와 이에야스에 의해 계속되었습니다. 그의 좌우명 "텐카후부"(천하포무—힘으로 천하를)는 필요한 어떤 수단을 통해서라도 달성되는 통일된 일본에 대한 그의 비전을 구현했습니다.""",
    traits_en=["Ruthless", "Innovative", "Brilliant", "Ambitious", "Revolutionary"],
    traits_ko=["무자비한", "혁신적인", "뛰어난", "야망적인", "혁명적인"],
    story_en="At the Battle of Okehazama, Nobunaga faced Imagawa Yoshimoto's army of 25,000 with only 3,000 men. Rather than fight defensively, he launched a surprise attack during a thunderstorm, killing Yoshimoto and scattering his army—turning an impossible situation into legendary victory.",
    story_ko="오케하자마 전투에서, 노부나가는 단 3,000명으로 이마가와 요시모토의 25,000 군대에 맞섰습니다. 방어적으로 싸우기보다, 그는 뇌우 중에 기습 공격을 감행하여 요시모토를 죽이고 그의 군대를 흩뜨렸습니다—불가능한 상황을 전설적인 승리로 바꾸었습니다.",
    match_message_en="Your features carry the fierce ambition of Nobunaga. There is a revolutionary, unstoppable quality to your presence—the look of one who will change the world by sheer force of will.",
    match_message_ko="당신의 이목구비는 노부나가의 맹렬한 야망을 담고 있습니다. 당신의 존재에는 혁명적이고 멈출 수 없는 품질이 있습니다—순수한 의지의 힘으로 세상을 바꿀 사람의 모습.",
    image_prompt="Fierce Japanese warlord in battle armor, intense commanding gaze, surrounded by firearms and banners, flames and war in background, revolutionary warrior presence",
    visual_description="Sharp fierce features, intense ambitious eyes, commanding warrior bearing, expression of absolute determination and revolutionary fire",
    aliases=["織田信長", "Demon King", "The Fool of Owari"],
    era="Sengoku Period (1534-1582)",
    related_characters=["toyotomi_hideyoshi", "tokugawa_ieyasu", "akechi_mitsuhide"]
)


IZANAGI_DESC = CharacterDescription(
    id="izanagi",
    name_en="Izanagi",
    name_ko="이자나기",
    tagline_en="Creator God, Father of Japan",
    tagline_ko="창조신, 일본의 아버지",
    description_en="""Izanagi-no-Mikoto is the primordial god who, together with his wife Izanami, created the Japanese islands and birthed the gods. Standing on the Floating Bridge of Heaven, they stirred the ocean with a jeweled spear, and the drops that fell formed the first island.

When Izanami died giving birth to the fire god, Izanagi descended to Yomi (the underworld) to retrieve her. But when he saw her rotting form, he fled in horror, and she chased him with demons. He sealed the entrance to Yomi with a boulder, and they exchanged words of eternal separation.

Upon returning to the surface, Izanagi purified himself in a river. From this purification were born the three most important kami: Amaterasu from his left eye, Tsukuyomi from his right eye, and Susanoo from his nose.""",
    description_ko="""이자나기노미코토는 아내 이자나미와 함께 일본 열도를 창조하고 신들을 낳은 원초적 신입니다. 하늘의 떠다니는 다리에 서서, 그들은 보석 창으로 바다를 저었고, 떨어진 물방울들이 첫 번째 섬을 형성했습니다.

이자나미가 불의 신을 낳다 죽었을 때, 이자나기는 그녀를 데려오기 위해 요미(지하세계)로 내려갔습니다. 그러나 그녀의 썩은 모습을 보았을 때, 그는 공포에 질려 도망쳤고, 그녀는 악마들과 함께 그를 쫓았습니다. 그는 바위로 요미의 입구를 봉인했고, 그들은 영원한 이별의 말을 교환했습니다.

지상으로 돌아온 후, 이자나기는 강에서 자신을 정화했습니다. 이 정화에서 세 가지 가장 중요한 카미가 태어났습니다: 왼쪽 눈에서 아마테라스, 오른쪽 눈에서 츠쿠요미, 코에서 스사노오.""",
    traits_en=["Creative", "Grieving", "Primal", "Life-giving", "Purifying"],
    traits_ko=["창조적인", "슬퍼하는", "원초적인", "생명을 주는", "정화하는"],
    story_en="When Izanagi lit a torch to see his wife in Yomi, he saw maggots crawling through her body and the eight thunder gods dwelling within her. She screamed that he had shamed her, and sent the hags of Yomi to catch him. He threw objects that transformed into distractions, barely escaping.",
    story_ko="이자나기가 요미에서 아내를 보기 위해 횃불을 켰을 때, 그녀의 몸을 기어다니는 구더기들과 그녀 안에 거하는 여덟 번개 신들을 보았습니다. 그녀는 그가 자신을 수치스럽게 했다고 소리쳤고, 요미의 마녀들을 보내 그를 잡게 했습니다. 그는 주의를 분산시키는 것으로 변하는 물건들을 던지며 간신히 탈출했습니다.",
    match_message_en="Your features carry the creative power of Izanagi. There is a primal, life-giving quality to your presence—the look of one who brings new worlds into being.",
    match_message_ko="당신의 이목구비는 이자나기의 창조적 힘을 담고 있습니다. 당신의 존재에는 원초적이고 생명을 주는 품질이 있습니다—새로운 세상을 존재하게 하는 사람의 모습.",
    image_prompt="Primordial Japanese creator god with jeweled spear, standing on heavenly bridge above ocean, divine robes, creating islands, sunrise behind, mythic origin scene",
    visual_description="Ancient noble features, eyes of creation and loss, dignified bearing, expression of creative power mixed with eternal grief",
    aliases=["伊邪那岐", "Izanagi-no-Mikoto", "He Who Invites"],
    era="Japanese Mythology",
    related_characters=["izanami", "amaterasu", "tsukuyomi", "susanoo"]
)

IZANAMI_DESC = CharacterDescription(
    id="izanami",
    name_en="Izanami",
    name_ko="이자나미",
    tagline_en="Creator Goddess, Queen of the Underworld",
    tagline_ko="창조 여신, 지하세계의 여왕",
    description_en="""Izanami-no-Mikoto is the primordial goddess who, with her husband Izanagi, created Japan and birthed the gods. After creating the islands and many deities, she died giving birth to Kagutsuchi, the fire god, and descended to Yomi, the land of the dead.

When Izanagi came to retrieve her, she had already eaten the food of the underworld and could not fully return. She asked him to wait while she negotiated with the gods of Yomi, but he couldn't wait and lit a torch—seeing her rotting corpse covered in maggots and thunder gods.

Humiliated and enraged, Izanami transformed into the Queen of Yomi, vowing to kill 1,000 people each day. Izanagi responded that he would then cause 1,500 to be born—and thus life and death became intertwined forever.""",
    description_ko="""이자나미노미코토는 남편 이자나기와 함께 일본을 창조하고 신들을 낳은 원초적 여신입니다. 섬들과 많은 신들을 창조한 후, 그녀는 불의 신 카구츠치를 낳다 죽어 죽은 자들의 땅인 요미로 내려갔습니다.

이자나기가 그녀를 데려오려 왔을 때, 그녀는 이미 지하세계의 음식을 먹어서 완전히 돌아올 수 없었습니다. 그녀는 요미의 신들과 협상하는 동안 기다려달라고 했지만, 그는 기다리지 못하고 횃불을 켰습니다—구더기와 번개 신들로 뒤덮인 그녀의 썩은 시체를 보았습니다.

굴욕감과 분노에 사로잡힌 이자나미는 요미의 여왕으로 변신하여 매일 1,000명을 죽이겠다고 맹세했습니다. 이자나기는 그러면 1,500명이 태어나게 하겠다고 응답했고—이렇게 삶과 죽음은 영원히 얽히게 되었습니다.""",
    traits_en=["Creative", "Transformative", "Dark", "Powerful", "Grieving"],
    traits_ko=["창조적인", "변형하는", "어두운", "강력한", "슬퍼하는"],
    story_en="Before becoming Queen of Yomi, Izanami was a loving creator. The tragedy of her death and Izanagi's betrayal of her trust transformed her into something darker—a reminder that even the most loving beings can be changed by death and abandonment.",
    story_ko="요미의 여왕이 되기 전, 이자나미는 사랑스러운 창조자였습니다. 그녀의 죽음과 이자나기의 신뢰 배신의 비극은 그녀를 더 어두운 것으로 변형시켰습니다—가장 사랑스러운 존재도 죽음과 버림받음에 의해 변할 수 있다는 것을 상기시킵니다.",
    match_message_en="Your features reflect the dark power of Izanami. There is a transformative, underworld quality to your presence—the look of one who has passed through death and emerged changed.",
    match_message_ko="당신의 이목구비는 이자나미의 어두운 힘을 반영합니다. 당신의 존재에는 변형하는 지하세계의 품질이 있습니다—죽음을 통과하여 변화된 채로 나온 사람의 모습.",
    image_prompt="Dark Japanese goddess of death, beautiful but with shadows, underworld queen in decayed elegant robes, entrance to Yomi behind, both creator and destroyer, tragic beauty",
    visual_description="Haunting beautiful features, eyes of grief and darkness, once-radiant now shadowed, expression of tragic transformation",
    aliases=["伊邪那美", "Izanami-no-Mikoto", "She Who Invites"],
    era="Japanese Mythology",
    related_characters=["izanagi", "kagutsuchi", "amaterasu"]
)

EBISU_DESC = CharacterDescription(
    id="ebisu",
    name_en="Ebisu",
    name_ko="에비스",
    tagline_en="God of Fishermen and Luck",
    tagline_ko="어부와 행운의 신",
    description_en="""Ebisu is the only one of the Seven Lucky Gods who originated purely in Japan. He is the patron of fishermen, merchants, and good fortune, always depicted with a fishing rod, a sea bream (tai), and a cheerful smile.

According to legend, Ebisu was born without bones (or as a leech child) and cast into the sea by his parents Izanagi and Izanami. Despite this cruel beginning, he survived, grew strong, and became the beloved god of prosperity and good luck. His perseverance through hardship is seen as his greatest virtue.

Ebisu is deaf, which is why he doesn't hear the call to gather with other gods in October. He remains to bless those who stayed behind, and his festivals are held when other gods are absent.""",
    description_ko="""에비스는 칠복신 중 유일하게 순수하게 일본에서 기원한 신입니다. 그는 어부, 상인, 행운의 수호자로, 항상 낚싯대, 도미(타이), 밝은 미소와 함께 묘사됩니다.

전설에 따르면, 에비스는 뼈가 없이 (또는 거머리 아이로) 태어나 부모 이자나기와 이자나미에 의해 바다에 버려졌습니다. 이 잔인한 시작에도 불구하고, 그는 살아남아 강해졌고, 사랑받는 번영과 행운의 신이 되었습니다. 고난을 통한 그의 인내심은 그의 가장 큰 미덕으로 여겨집니다.

에비스는 귀가 멀어서 10월에 다른 신들이 모이는 소집을 듣지 못합니다. 그는 남아서 남겨진 이들을 축복하며, 그의 축제는 다른 신들이 없을 때 열립니다.""",
    traits_en=["Lucky", "Persevering", "Cheerful", "Generous", "Resilient"],
    traits_ko=["운이 좋은", "인내하는", "쾌활한", "관대한", "회복력 있는"],
    story_en="Fishermen in Japan would throw back the first fish they caught as an offering to Ebisu, believing he would reward their generosity with a larger catch. His smile on rough seas was said to calm the waves and guide ships safely to shore.",
    story_ko="일본의 어부들은 잡은 첫 번째 물고기를 에비스에게 제물로 다시 던지며, 그가 그들의 관대함에 더 큰 어획으로 보답할 것이라 믿었습니다. 거친 바다에서 그의 미소는 파도를 잠재우고 배를 안전하게 해안으로 인도한다고 합니다.",
    match_message_en="Your features reflect the cheerful luck of Ebisu. There is a resilient, fortunate quality to your presence—the look of one who overcomes hardship with a smile.",
    match_message_ko="당신의 이목구비는 에비스의 쾌활한 행운을 반영합니다. 당신의 존재에는 회복력 있고 운이 좋은 품질이 있습니다—미소로 고난을 극복하는 사람의 모습.",
    image_prompt="Cheerful Japanese god with fishing rod and large sea bream, happy laughing face, traditional festive attire, ocean background, lucky and prosperous aura, warm welcoming presence",
    visual_description="Round cheerful features, smiling eyes, warm friendly expression, look of resilient optimism and good fortune",
    aliases=["恵比寿", "Hiruko", "Yebisu"],
    era="Japanese Mythology",
    related_characters=["izanagi", "izanami", "seven_lucky_gods"]
)

BISHAMON_DESC = CharacterDescription(
    id="bishamon",
    name_en="Bishamonten",
    name_ko="비샤몬텐",
    tagline_en="God of War and Protector of the Righteous",
    tagline_ko="전쟁의 신, 정의로운 자의 수호자",
    description_en="""Bishamonten is the god of warriors, punisher of evildoers, and one of the Seven Lucky Gods. Originally the Hindu deity Vaiśravaṇa, he became one of the Four Heavenly Kings in Buddhism and was adopted into Japanese religion as a protector and bringer of fortune.

Unlike mere war gods, Bishamonten represents righteous warfare—the defense of the innocent and punishment of evil. He is depicted in full armor, carrying a pagoda in one hand (representing the treasure house of faith) and a trident or spear in the other.

Samurai prayed to Bishamonten before battle, not for victory at any cost, but for the courage and righteousness to fight justly. He is the patron of warriors who fight for honor rather than greed.""",
    description_ko="""비샤몬텐은 전사들의 신, 악인의 처벌자, 칠복신 중 하나입니다. 원래 힌두 신 바이슈라바나였으며, 불교에서 사천왕 중 하나가 되었고 보호자와 행운을 가져다주는 자로 일본 종교에 채택되었습니다.

단순한 전쟁 신과 달리, 비샤몬텐은 정의로운 전쟁—무고한 자의 방어와 악의 처벌—을 대표합니다. 그는 완전한 갑옷을 입고, 한 손에는 탑(신앙의 보물 창고를 나타내는)을, 다른 손에는 삼지창이나 창을 들고 있는 모습으로 묘사됩니다.

사무라이들은 전투 전에 비샤몬텐에게 기도했습니다, 어떤 대가를 치르더라도 승리를 위해서가 아니라, 정당하게 싸울 용기와 정의로움을 위해서. 그는 탐욕보다 명예를 위해 싸우는 전사들의 수호자입니다.""",
    traits_en=["Righteous", "Protective", "Warrior", "Just", "Powerful"],
    traits_ko=["정의로운", "보호하는", "전사적인", "공정한", "강력한"],
    story_en="Uesugi Kenshin, one of Japan's greatest warlords, considered himself the avatar of Bishamonten. Before every battle, he prayed at the god's shrine and fought with the conviction that his cause was just—making him nearly invincible on the battlefield.",
    story_ko="일본의 가장 위대한 전쟁 영주 중 하나인 우에스기 켄신은 자신을 비샤몬텐의 화신으로 여겼습니다. 모든 전투 전에 그는 신의 신사에서 기도했고 자신의 대의가 정당하다는 확신으로 싸웠습니다—그를 전장에서 거의 무적으로 만들었습니다.",
    match_message_en="Your features carry the righteous power of Bishamonten. There is a protective, warrior quality to your presence—the look of one who fights for justice, not conquest.",
    match_message_ko="당신의 이목구비는 비샤몬텐의 정의로운 힘을 담고 있습니다. 당신의 존재에는 보호하는 전사적 품질이 있습니다—정복이 아닌 정의를 위해 싸우는 사람의 모습.",
    image_prompt="Fierce Japanese war god in ornate armor, holding pagoda and trident, guardian stance, righteous warrior presence, golden and black armor, protective aura",
    visual_description="Fierce noble features, eyes of righteous fury, armored warrior bearing, expression of protective strength and justice",
    aliases=["毘沙門天", "Vaiśravaṇa", "Tamonten"],
    era="Japanese Mythology",
    related_characters=["uesugi_kenshin", "four_heavenly_kings", "seven_lucky_gods"]
)

TOYOTOMI_HIDEYOSHI_DESC = CharacterDescription(
    id="toyotomi_hideyoshi",
    name_en="Toyotomi Hideyoshi",
    name_ko="도요토미 히데요시",
    tagline_en="From Peasant to Ruler of All Japan",
    tagline_ko="농부에서 전일본의 지배자로",
    description_en="""Toyotomi Hideyoshi rose from being a peasant sandal-bearer to become the second great unifier of Japan and its supreme ruler. His rise was the most dramatic in Japanese history—proof that talent and cunning could overcome birth and tradition.

Starting as a servant of Oda Nobunaga, Hideyoshi proved himself through clever strategies and unwavering loyalty. After Nobunaga's assassination, Hideyoshi avenged him and continued the unification, conquering or diplomatically winning over all remaining opposition.

Despite his achievements, Hideyoshi was denied the title of Shogun due to his common birth. Instead, he took the title of Kampaku (Imperial Regent) and Taikō (retired Kampaku). His later years were marked by ambition gone too far, including invasions of Korea that ultimately failed.""",
    description_ko="""도요토미 히데요시는 농부 짚신 운반꾼에서 일본의 두 번째 대통일자이자 최고 통치자가 되었습니다. 그의 부상은 일본 역사상 가장 극적이었습니다—재능과 교활함이 출생과 전통을 극복할 수 있다는 증거.

오다 노부나가의 종으로 시작하여, 히데요시는 영리한 전략과 흔들림 없는 충성심으로 자신을 증명했습니다. 노부나가의 암살 후, 히데요시는 그를 복수하고 통일을 계속하여, 남은 모든 반대 세력을 정복하거나 외교적으로 이겼습니다.

그의 업적에도 불구하고, 히데요시는 평민 출신 때문에 쇼군 칭호를 거부당했습니다. 대신, 그는 캄파쿠(섭정)와 타이코(은퇴한 캄파쿠)의 칭호를 취했습니다. 말년은 궁극적으로 실패한 조선 침략을 포함하여 너무 멀리 간 야망으로 특징지어졌습니다.""",
    traits_en=["Cunning", "Ambitious", "Charismatic", "Self-made", "Strategic"],
    traits_ko=["교활한", "야망적인", "카리스마 있는", "자수성가한", "전략적인"],
    story_en="In winter, young Hideyoshi warmed Nobunaga's sandals by keeping them inside his clothes. This simple act of devotion caught Nobunaga's attention, and he began to rise. From such humble beginnings came the man who would rule all Japan.",
    story_ko="겨울에 어린 히데요시는 노부나가의 짚신을 옷 안에 넣어 따뜻하게 했습니다. 이 단순한 헌신의 행동이 노부나가의 주의를 끌었고, 그는 출세하기 시작했습니다. 이런 겸손한 시작에서 전 일본을 다스릴 사람이 나왔습니다.",
    match_message_en="Your features carry the cunning ambition of Hideyoshi. There is a self-made, unstoppable quality to your presence—the look of one who will rise no matter the obstacles.",
    match_message_ko="당신의 이목구비는 히데요시의 교활한 야망을 담고 있습니다. 당신의 존재에는 자수성가하고 멈출 수 없는 품질이 있습니다—장애물과 상관없이 오를 사람의 모습.",
    image_prompt="Japanese warlord who rose from peasant, clever alert expression, ornate armor befitting a ruler, holding golden gourd standard, cunning eyes, regal but common-born presence",
    visual_description="Alert clever features, sharp calculating eyes, bearing of earned authority, expression of cunning ambition and hard-won power",
    aliases=["豊臣秀吉", "Taikō", "Monkey (childhood)"],
    era="Sengoku-Azuchi-Momoyama Period (1537-1598)",
    related_characters=["oda_nobunaga", "tokugawa_ieyasu"]
)

TOKUGAWA_IEYASU_DESC = CharacterDescription(
    id="tokugawa_ieyasu",
    name_en="Tokugawa Ieyasu",
    name_ko="도쿠가와 이에야스",
    tagline_en="The Patient Victor, Founder of the Tokugawa Shogunate",
    tagline_ko="인내의 승리자, 도쿠가와 막부의 창시자",
    description_en="""Tokugawa Ieyasu was the third and final great unifier of Japan, founding the Tokugawa Shogunate that would rule Japan for over 250 years of peace. While Nobunaga and Hideyoshi forged the path, Ieyasu waited patiently—and ultimately won everything.

Spending years as a hostage in his youth, then decades as an ally (and rival) to Nobunaga and Hideyoshi, Ieyasu learned the value of patience and careful planning. After Hideyoshi's death, he maneuvered his way to the decisive Battle of Sekigahara, winning through superior strategy and key betrayals from enemy forces.

The Japanese saying goes: "Nobunaga piled the rice, Hideyoshi kneaded the dough, and Ieyasu ate the cake." His patience and longevity allowed him to outlive his rivals and build a lasting peace.""",
    description_ko="""도쿠가와 이에야스는 일본의 세 번째이자 마지막 대통일자로, 250년 이상의 평화를 다스릴 도쿠가와 막부를 창시했습니다. 노부나가와 히데요시가 길을 닦는 동안, 이에야스는 인내심 있게 기다렸고—궁극적으로 모든 것을 이겼습니다.

어린 시절 인질로 수년을, 그 후 노부나가와 히데요시의 동맹(그리고 경쟁자)으로 수십 년을 보내며, 이에야스는 인내와 신중한 계획의 가치를 배웠습니다. 히데요시의 사후, 그는 결정적인 세키가하라 전투로 기동하여, 우월한 전략과 적군의 핵심 배신을 통해 승리했습니다.

일본 속담에 "노부나가가 쌀을 쌓고, 히데요시가 반죽을 치대고, 이에야스가 떡을 먹었다"고 합니다. 그의 인내와 장수는 경쟁자들보다 오래 살고 지속적인 평화를 건설하게 했습니다.""",
    traits_en=["Patient", "Strategic", "Enduring", "Wise", "Victorious"],
    traits_ko=["인내하는", "전략적인", "지속하는", "지혜로운", "승리하는"],
    story_en="There's a famous story comparing the three unifiers: Asked what to do with a bird that won't sing, Nobunaga said 'Kill it,' Hideyoshi said 'Make it want to sing,' but Ieyasu said 'Wait for it to sing.' This patience defined his path to power.",
    story_ko="세 통일자를 비교하는 유명한 이야기가 있습니다: 울지 않는 새를 어떻게 할 것인지 물었을 때, 노부나가는 '죽여라', 히데요시는 '울게 만들어라'라고 했지만, 이에야스는 '울 때까지 기다려라'라고 했습니다. 이 인내심이 그의 권력으로 가는 길을 정의했습니다.",
    match_message_en="Your features reflect the patient wisdom of Ieyasu. There is an enduring, strategic quality to your presence—the look of one who knows that time itself can be the greatest weapon.",
    match_message_ko="당신의 이목구비는 이에야스의 인내하는 지혜를 반영합니다. 당신의 존재에는 지속하고 전략적인 품질이 있습니다—시간 자체가 가장 큰 무기가 될 수 있음을 아는 사람의 모습.",
    image_prompt="Elder Japanese shogun in formal attire, patient wise expression, Tokugawa crest, seated in position of supreme authority, dignified age, calm victorious presence",
    visual_description="Wise weathered features, patient calculating eyes, bearing of ultimate authority, expression of patient wisdom and final victory",
    aliases=["徳川家康", "Tōshō Daigongen", "The Old Tanuki"],
    era="Sengoku-Edo Period (1543-1616)",
    related_characters=["oda_nobunaga", "toyotomi_hideyoshi"]
)

MOMOTARO_DESC = CharacterDescription(
    id="momotaro",
    name_en="Momotarō",
    name_ko="모모타로",
    tagline_en="The Peach Boy, Hero of Japan",
    tagline_ko="복숭아 소년, 일본의 영웅",
    description_en="""Momotarō, the Peach Boy, is Japan's most beloved folk hero. Born from a giant peach floating down a river, he was discovered by an elderly childless couple who raised him as their own. He grew to be extraordinarily strong and pure of heart.

When demons (oni) from Onigashima (Demon Island) terrorized the land, young Momotarō set out to defeat them. Along the way, he befriended a dog, a monkey, and a pheasant by sharing his millet dumplings (kibidango). Together, this unlikely band defeated the demons and brought back their treasure.

Momotarō represents the Japanese ideal of a hero: brave but kind, strong but humble, and successful through building friendships and cooperation rather than brute force alone.""",
    description_ko="""모모타로, 복숭아 소년은 일본에서 가장 사랑받는 민간 영웅입니다. 강을 따라 떠내려오는 거대한 복숭아에서 태어나, 아이가 없던 노부부에게 발견되어 그들의 자식으로 자랐습니다. 그는 비범하게 강하고 마음이 순수하게 자랐습니다.

오니가시마(도깨비 섬)의 도깨비(오니)들이 땅을 공포에 떨게 했을 때, 어린 모모타로는 그들을 물리치기 위해 떠났습니다. 길에서 그는 자신의 기비당고(수수 경단)를 나눠주며 개, 원숭이, 꿩과 친구가 되었습니다. 함께, 이 특이한 무리는 도깨비들을 물리치고 그들의 보물을 가져왔습니다.

모모타로는 영웅의 일본적 이상을 대표합니다: 용감하지만 친절하고, 강하지만 겸손하며, 무력만이 아닌 우정과 협력을 통해 성공합니다.""",
    traits_en=["Brave", "Kind", "Pure", "Cooperative", "Heroic"],
    traits_ko=["용감한", "친절한", "순수한", "협력적인", "영웅적인"],
    story_en="When Momotarō met the dog, monkey, and pheasant, each initially wanted to fight him. Instead of battling, he offered to share his food. This act of generosity transformed potential enemies into loyal friends who helped him achieve what he couldn't alone.",
    story_ko="모모타로가 개, 원숭이, 꿩을 만났을 때, 각각은 처음에 그와 싸우려 했습니다. 싸우는 대신, 그는 음식을 나누겠다고 제안했습니다. 이 관대함의 행동은 잠재적 적들을 혼자서는 달성할 수 없는 것을 도와준 충성스러운 친구로 변화시켰습니다.",
    match_message_en="Your features carry the pure heroism of Momotarō. There is a brave, kind quality to your presence—the look of one who defeats evil through courage and friendship.",
    match_message_ko="당신의 이목구비는 모모타로의 순수한 영웅주의를 담고 있습니다. 당신의 존재에는 용감하고 친절한 품질이 있습니다—용기와 우정을 통해 악을 물리치는 사람의 모습.",
    image_prompt="Young Japanese hero with headband, accompanied by dog monkey and pheasant, carrying banner, peach motif, bright heroic pose, setting sail for Demon Island",
    visual_description="Youthful noble features, bright determined eyes, heroic bearing, expression of pure-hearted courage and kindness",
    aliases=["桃太郎", "Peach Boy", "The Peach Prince"],
    era="Japanese Folklore",
    related_characters=["oni"]
)

UESUGI_KENSHIN_DESC = CharacterDescription(
    id="uesugi_kenshin",
    name_en="Uesugi Kenshin",
    name_ko="우에스기 켄신",
    tagline_en="The Dragon of Echigo, God of War Incarnate",
    tagline_ko="에치고의 용, 군신의 화신",
    description_en="""Uesugi Kenshin was one of Japan's most powerful warlords during the Sengoku period, known as the "Dragon of Echigo" for his military prowess. A devout Buddhist and worshipper of Bishamonten, he believed himself to be the avatar of the war god.

Unlike other warlords who fought for land and power, Kenshin often fought to uphold justice and righteousness. His legendary rivalry with Takeda Shingen produced five inconclusive Battles of Kawanakajima, considered the greatest samurai battles in Japanese history.

Kenshin was known for his administrative skills, sake drinking, and possibly being asexual or secretly female. He died suddenly at age 49, supposedly of stomach cancer or assassination, leaving his territory to civil war among his adopted heirs.""",
    description_ko="""우에스기 켄신은 전국시대 일본의 가장 강력한 전쟁 영주 중 하나로, 군사적 능력으로 "에치고의 용"으로 알려졌습니다. 독실한 불교도이자 비샤몬텐 숭배자로, 그는 자신이 군신의 화신이라고 믿었습니다.

토지와 권력을 위해 싸운 다른 전쟁 영주들과 달리, 켄신은 종종 정의와 의로움을 지키기 위해 싸웠습니다. 타케다 신겐과의 전설적인 라이벌 관계는 일본 역사상 가장 위대한 사무라이 전투로 여겨지는 5번의 결론 없는 가와나카지마 전투를 낳았습니다.

켄신은 행정 능력, 술 마시기, 그리고 아마도 무성애자이거나 비밀리에 여성이었을 수 있다는 것으로 알려졌습니다. 그는 49세에 갑자기 죽었는데, 아마도 위암이나 암살로, 그의 영토를 양자들 사이의 내전에 남겼습니다.""",
    traits_en=["Righteous", "Fierce", "Devout", "Honorable", "Legendary"],
    traits_ko=["정의로운", "맹렬한", "독실한", "명예로운", "전설적인"],
    story_en="In the fourth Battle of Kawanakajima, Kenshin personally charged into Shingen's command camp and attacked him with his sword. Shingen famously defended himself with his iron war fan. This single combat between rival lords became legendary in Japanese history.",
    story_ko="네 번째 가와나카지마 전투에서, 켄신은 직접 신겐의 지휘소로 돌진하여 검으로 그를 공격했습니다. 신겐은 유명하게 철제 군배로 자신을 방어했습니다. 라이벌 영주들 간의 이 일대일 전투는 일본 역사에서 전설이 되었습니다.",
    match_message_en="Your features carry the righteous fury of Uesugi Kenshin. There is a divine warrior quality to your presence—the look of one who fights as an avatar of justice itself.",
    match_message_ko="당신의 이목구비는 우에스기 켄신의 정의로운 분노를 담고 있습니다. 당신의 존재에는 신성한 전사의 품질이 있습니다—정의 자체의 화신으로 싸우는 사람의 모습.",
    image_prompt="Japanese warlord in white robes and armor, prayer beads, dragon motif, riding into battle, devotional and fierce, Bishamonten's avatar, legendary warrior presence",
    visual_description="Noble fierce features, blazing righteous eyes, warrior-monk bearing, expression of divine fury and unwavering justice",
    aliases=["上杉謙信", "Dragon of Echigo", "Nagao Kagetora"],
    era="Sengoku Period (1530-1578)",
    related_characters=["takeda_shingen", "oda_nobunaga", "bishamonten"]
)

KAGUYA_HIME_DESC = CharacterDescription(
    id="kaguya_hime",
    name_en="Kaguya-hime",
    name_ko="카구야 공주",
    tagline_en="The Moon Princess, The Shining One",
    tagline_ko="달의 공주, 빛나는 자",
    description_en="""Kaguya-hime, the Princess of the Moon, is the heroine of Japan's oldest prose narrative, The Tale of the Bamboo Cutter. Found as a tiny baby inside a glowing bamboo stalk by an elderly bamboo cutter, she grew into a woman of supernatural beauty.

Five nobles and even the Emperor sought her hand in marriage, but she set impossible tasks for each suitor. She asked for Buddha's stone begging bowl, a jeweled branch from Mount Hōrai, the fire-rat's robe, a dragon's neck jewel, and a cowrie shell from a swallow's nest. All failed.

Kaguya-hime was not of this world—she came from the Moon, sent to Earth as punishment. When the Moon's emissaries came to take her back, she left behind a robe of feathers and an elixir of immortality for the Emperor, who burned them on Japan's highest mountain, giving it the name Fuji (immortal).""",
    description_ko="""카구야 공주, 달의 공주는 일본 최초의 산문 서사인 타케토리 모노가타리의 여주인공입니다. 노인 대나무 꾼이 빛나는 대나무 줄기 안에서 작은 아기로 발견하여, 그녀는 초자연적 아름다움의 여인으로 자랐습니다.

다섯 귀족과 심지어 천황까지 그녀에게 청혼했지만, 그녀는 각 구혼자에게 불가능한 과제를 설정했습니다. 그녀는 부처의 돌 탁발 그릇, 호라이산의 보석 가지, 불쥐의 가죽옷, 용의 목 보석, 제비 둥지의 조개껍데기를 요청했습니다. 모두 실패했습니다.

카구야 공주는 이 세상의 존재가 아니었습니다—그녀는 벌로 지구에 보내진 달에서 왔습니다. 달의 사자들이 그녀를 데려가러 왔을 때, 그녀는 천황에게 깃털 옷과 불로장생의 영약을 남겼고, 천황은 그것들을 일본의 가장 높은 산에서 태워 후지(불사)라는 이름을 붙였습니다.""",
    traits_en=["Ethereal", "Mysterious", "Unattainable", "Otherworldly", "Melancholic"],
    traits_ko=["공기 같은", "신비로운", "도달할 수 없는", "이세계의", "우울한"],
    story_en="When the Moon's emissaries came in a cloud chariot, Kaguya-hime wept as she prepared to leave. She wrote farewell letters to her earthly parents and the Emperor, expressing her sorrow at leaving the world she had grown to love. Donning the celestial robe, she forgot all earthly memories and ascended to the Moon.",
    story_ko="달의 사자들이 구름 마차를 타고 왔을 때, 카구야 공주는 떠날 준비를 하며 울었습니다. 그녀는 지상의 부모와 천황에게 작별 편지를 써서 사랑하게 된 세상을 떠나는 슬픔을 표현했습니다. 천상의 옷을 입자, 그녀는 모든 지상의 기억을 잊고 달로 올라갔습니다.",
    match_message_en="Your features reflect the ethereal beauty of Kaguya-hime. There is an otherworldly, unattainable quality to your presence—the look of one who belongs to the Moon itself.",
    match_message_ko="당신의 이목구비는 카구야 공주의 공기 같은 아름다움을 반영합니다. 당신의 존재에는 이세계의 도달할 수 없는 품질이 있습니다—달 자체에 속하는 사람의 모습.",
    image_prompt="Ethereal Japanese princess in glowing white robes, moon background, bamboo around her, supernatural beauty, tears of farewell, celestial beings approaching, otherworldly grace",
    visual_description="Ethereal otherworldly beauty, luminous features, sad knowing eyes, expression of transcendent beauty and melancholic farewell",
    aliases=["かぐや姫", "Nayotake-no-Kaguya-hime", "Princess of the Moon"],
    era="Japanese Folklore",
    related_characters=["emperor", "bamboo_cutter"]
)

TAKEDA_SHINGEN_DESC = CharacterDescription(
    id="takeda_shingen",
    name_en="Takeda Shingen",
    name_ko="타케다 신겐",
    tagline_en="The Tiger of Kai, Master of War",
    tagline_ko="카이의 호랑이, 전쟁의 대가",
    description_en="""Takeda Shingen was one of the most feared warlords of Japan's Sengoku period, known as the "Tiger of Kai" for his ferocity and tactical brilliance. His cavalry charges and innovative strategies made his enemies tremble.

Shingen's greatest rivalry was with Uesugi Kenshin, the "Dragon of Echigo." Their five Battles of Kawanakajima are considered the pinnacle of samurai warfare. The famous phrase "Fu-Rin-Ka-Zan" (Swift as Wind, Silent as Forest, Fierce as Fire, Immovable as Mountain) was Shingen's battle standard, taken from Sun Tzu's Art of War.

Had Shingen not died of illness while marching on Kyoto, many believe he could have unified Japan before Nobunaga. His death allowed Nobunaga's rise, changing Japanese history forever.""",
    description_ko="""타케다 신겐은 전국시대 일본에서 가장 두려움 받는 전쟁 영주 중 하나로, 그의 맹렬함과 전술적 탁월함으로 "카이의 호랑이"로 알려졌습니다. 그의 기병 돌격과 혁신적인 전략은 적들을 떨게 했습니다.

신겐의 가장 큰 라이벌 관계는 "에치고의 용" 우에스기 켄신과의 것이었습니다. 그들의 다섯 번의 가와나카지마 전투는 사무라이 전쟁의 정점으로 여겨집니다. 유명한 문구 "풍림화산"(바람처럼 빠르게, 숲처럼 조용하게, 불처럼 맹렬하게, 산처럼 움직이지 않게)은 손자의 손자병법에서 따온 신겐의 전투 깃발이었습니다.

신겐이 교토로 진군하는 중 병으로 죽지 않았다면, 많은 사람들은 그가 노부나가보다 먼저 일본을 통일할 수 있었다고 믿습니다. 그의 죽음이 노부나가의 부상을 허용하여 일본 역사를 영원히 바꾸었습니다.""",
    traits_en=["Tactical", "Fierce", "Brilliant", "Feared", "Legendary"],
    traits_ko=["전술적인", "맹렬한", "뛰어난", "두려움 받는", "전설적인"],
    story_en="When Shingen marched toward Kyoto, Oda Nobunaga sent him a gift of gold as appeasement. It failed—Shingen continued his advance. Only his death from illness stopped him, and it's said Nobunaga secretly rejoiced at the news.",
    story_ko="신겐이 교토를 향해 진군했을 때, 오다 노부나가는 화해의 의미로 금을 선물로 보냈습니다. 실패했습니다—신겐은 전진을 계속했습니다. 오직 병으로 인한 그의 죽음만이 그를 멈췄고, 노부나가는 그 소식에 비밀리에 기뻐했다고 합니다.",
    match_message_en="Your features carry the tactical brilliance of Takeda Shingen. There is a tiger-like quality to your presence—the look of one who masters both strategy and ferocity.",
    match_message_ko="당신의 이목구비는 타케다 신겐의 전술적 탁월함을 담고 있습니다. 당신의 존재에는 호랑이 같은 품질이 있습니다—전략과 맹렬함 모두를 숙달한 사람의 모습.",
    image_prompt="Fierce Japanese warlord with tiger imagery, banner reading Fu-Rin-Ka-Zan, commanding cavalry charge, tactical genius presence, armor with red accents, legendary warrior",
    visual_description="Fierce commanding features, calculating tiger-like eyes, warrior strategist bearing, expression of tactical brilliance and overwhelming force",
    aliases=["武田信玄", "Tiger of Kai", "Takeda Harunobu"],
    era="Sengoku Period (1521-1573)",
    related_characters=["uesugi_kenshin", "oda_nobunaga"]
)


# Dictionary of Japanese descriptions
JAPANESE_DESCRIPTIONS = {
    "amaterasu": AMATERASU_DESC,
    "susanoo": SUSANOO_DESC,
    "tsukuyomi": TSUKUYOMI_DESC,
    "inari": INARI_DESC,
    "kitsune": KITSUNE_DESC,
    "raijin": RAIJIN_DESC,
    "fujin": FUJIN_DESC,
    "benzaiten": BENZAITEN_DESC,
    "miyamoto_musashi": MIYAMOTO_MUSASHI_DESC,
    "oda_nobunaga": ODA_NOBUNAGA_DESC,
    "izanagi": IZANAGI_DESC,
    "izanami": IZANAMI_DESC,
    "ebisu": EBISU_DESC,
    "bishamon": BISHAMON_DESC,
    "toyotomi_hideyoshi": TOYOTOMI_HIDEYOSHI_DESC,
    "tokugawa_ieyasu": TOKUGAWA_IEYASU_DESC,
    "momotaro": MOMOTARO_DESC,
    "uesugi_kenshin": UESUGI_KENSHIN_DESC,
    "kaguya_hime": KAGUYA_HIME_DESC,
    "takeda_shingen": TAKEDA_SHINGEN_DESC,
}

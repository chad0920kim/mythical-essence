"""
Roman Mythology Character Descriptions
Contains detailed descriptions for Roman mythological figures
"""
from .descriptions import CharacterDescription


JUPITER_DESC = CharacterDescription(
    id="jupiter",
    name_en="Jupiter",
    name_ko="유피테르",
    tagline_en="King of the Roman Gods, Lord of Sky and Thunder",
    tagline_ko="로마 신들의 왕, 하늘과 천둥의 지배자",
    description_en="""Jupiter is the supreme deity of the Roman pantheon, equivalent to the Greek Zeus but with distinct Roman characteristics. As the god of sky and thunder, he wielded the lightning bolt as his weapon and symbol of absolute divine authority.

The Romans considered Jupiter the protector of the state, laws, and social order. His temple on Capitoline Hill was the most important in Rome, where victorious generals would offer thanks and where the most sacred oaths were sworn.

Jupiter Optimus Maximus—"Jupiter Best and Greatest"—was the central figure of Roman state religion, embodying Roman virtues of justice, faithfulness, and the glory of Rome itself.""",
    description_ko="""유피테르는 로마 판테온의 최고신으로, 그리스의 제우스에 해당하지만 독특한 로마적 특성을 가지고 있습니다. 하늘과 천둥의 신으로서, 그는 절대적인 신성한 권위의 무기이자 상징으로 번개를 휘둘렀습니다.

로마인들은 유피테르를 국가, 법률, 사회 질서의 수호자로 여겼습니다. 카피톨리누스 언덕에 있는 그의 신전은 로마에서 가장 중요한 신전으로, 승리한 장군들이 감사를 드리고 가장 신성한 맹세가 행해지는 곳이었습니다.

유피테르 옵티무스 막시무스—"가장 좋고 가장 위대한 유피테르"—는 로마 국가 종교의 중심 인물로서, 정의, 충실함, 그리고 로마 자체의 영광이라는 로마의 덕목을 구현했습니다.""",
    traits_en=["Supreme", "Authoritative", "Just", "Protective", "Majestic"],
    traits_ko=["최고의", "권위있는", "공정한", "수호하는", "장엄한"],
    story_en="When Hannibal threatened Rome, the citizens prayed to Jupiter Optimus Maximus. Through sacrifice and devotion to Jupiter, Rome persevered through its darkest hours and eventually triumphed, proving the god's protection over the eternal city.",
    story_ko="한니발이 로마를 위협했을 때, 시민들은 유피테르 옵티무스 막시무스에게 기도했습니다. 유피테르에 대한 희생과 헌신을 통해, 로마는 가장 어두운 시간을 견뎌내고 결국 승리하여, 영원한 도시에 대한 신의 보호를 증명했습니다.",
    match_message_en="You carry the supreme authority of Jupiter. There is a majestic, protective quality to your presence—the look of one who upholds justice and guards the social order.",
    match_message_ko="당신은 유피테르의 최고 권위를 지니고 있습니다. 당신의 존재에는 장엄하고 수호하는 품질이 있습니다—정의를 수호하고 사회 질서를 지키는 사람의 모습.",
    image_prompt="Majestic Roman god-king on marble throne, holding lightning bolt and eagle scepter, wearing purple toga with golden oak crown, Capitoline temple background, divine Roman authority",
    visual_description="Powerful square jaw, commanding deep-set eyes, dignified Roman features, expression of supreme divine authority",
    aliases=["Jove", "Jupiter Optimus Maximus", "Iuppiter"],
    era="Ancient Rome",
    related_characters=["juno", "mars", "minerva"]
)

JUNO_DESC = CharacterDescription(
    id="juno",
    name_en="Juno",
    name_ko="유노",
    tagline_en="Queen of the Gods, Protector of Women and Marriage",
    tagline_ko="신들의 여왕, 여성과 결혼의 수호자",
    description_en="""Juno is the queen of the Roman gods and goddess of marriage, childbirth, and women. Wife of Jupiter, she was one of the most important deities in Roman religion, with temples and festivals dedicated to her protection of Roman women and the Roman state.

The month of June is named after Juno, and it remains the most popular month for weddings—a tradition dating back to Roman times when brides sought Juno's blessing. She was also Juno Moneta, protector of finances, whose temple housed Rome's mint.

Juno embodied the Roman ideal of the dignified matron—powerful, protective, and devoted to family and state. Her sacred animals were the peacock and goose, and she was often depicted with a diadem and scepter.""",
    description_ko="""유노는 로마 신들의 여왕이자 결혼, 출산, 여성의 여신입니다. 유피테르의 아내로서, 그녀는 로마 종교에서 가장 중요한 신들 중 하나였으며, 로마 여성과 로마 국가의 보호에 헌정된 신전과 축제가 있었습니다.

6월(June)은 유노의 이름을 따서 지어졌으며, 결혼식에 가장 인기 있는 달로 남아 있습니다—이 전통은 신부들이 유노의 축복을 구했던 로마 시대로 거슬러 올라갑니다. 그녀는 또한 재정의 수호자인 유노 모네타였으며, 그녀의 신전에는 로마의 조폐국이 있었습니다.

유노는 품위 있는 귀부인이라는 로마의 이상—강력하고, 보호하며, 가족과 국가에 헌신하는—을 구현했습니다. 그녀의 신성한 동물은 공작과 거위였으며, 왕관과 홀을 들고 있는 모습으로 자주 묘사되었습니다.""",
    traits_en=["Queenly", "Protective", "Dignified", "Maternal", "Powerful"],
    traits_ko=["여왕다운", "수호하는", "품위있는", "모성적인", "강력한"],
    story_en="Every year on the Matronalia, Roman women would receive gifts and pray to Juno for happy marriages and healthy children. Temples would be filled with offerings as the goddess blessed the sacred institution of Roman marriage.",
    story_ko="매년 마트로날리아에, 로마 여성들은 선물을 받고 유노에게 행복한 결혼과 건강한 자녀를 위해 기도했습니다. 여신이 로마 결혼의 신성한 제도를 축복할 때 신전은 봉헌물로 가득 찼습니다.",
    match_message_en="You possess the queenly dignity of Juno. There is a protective, maternal strength to your presence—the look of one who safeguards family and maintains sacred bonds.",
    match_message_ko="당신은 유노의 여왕다운 품위를 지니고 있습니다. 당신의 존재에는 보호하고 모성적인 힘이 있습니다—가족을 지키고 신성한 유대를 유지하는 사람의 모습.",
    image_prompt="Regal Roman goddess queen with peacock, wearing diadem and flowing robes, holding scepter, dignified maternal expression, temple of Juno background",
    visual_description="Regal oval face, dignified piercing eyes, noble Roman features, expression of queenly authority and maternal protection",
    aliases=["Juno Regina", "Juno Moneta", "Hera"],
    era="Ancient Rome",
    related_characters=["jupiter", "mars", "minerva"]
)

MARS_DESC = CharacterDescription(
    id="mars",
    name_en="Mars",
    name_ko="마르스",
    tagline_en="God of War and Guardian of Rome",
    tagline_ko="전쟁의 신이자 로마의 수호자",
    description_en="""Mars is the Roman god of war and second only to Jupiter in importance. Unlike the Greek Ares who represented war's brutality, Mars was a more dignified figure—the divine father of Romulus and Remus and thus ancestor of all Romans.

As the father of Rome's founders, Mars held special significance as the guardian of the Roman state and its military might. The month of March is named for him, and it was the traditional beginning of the military campaign season. Roman soldiers prayed to Mars before battle and dedicated spoils to him after victory.

Mars also had agricultural aspects, protecting crops and ensuring fertile fields. The Campus Martius (Field of Mars) in Rome was both a military training ground and a sacred space where armies gathered before marching to war.""",
    description_ko="""마르스는 로마의 전쟁의 신으로 유피테르 다음으로 중요합니다. 전쟁의 잔인함을 상징했던 그리스의 아레스와 달리, 마르스는 더 품위 있는 인물이었습니다—로물루스와 레무스의 신성한 아버지이자 따라서 모든 로마인의 조상이었습니다.

로마 건국자들의 아버지로서, 마르스는 로마 국가와 그 군사력의 수호자로서 특별한 의미를 가졌습니다. 3월(March)은 그의 이름을 따서 지어졌으며, 전통적으로 군사 원정 시즌의 시작이었습니다. 로마 병사들은 전투 전에 마르스에게 기도하고 승리 후에 전리품을 바쳤습니다.

마르스는 또한 농업적 측면이 있어, 작물을 보호하고 비옥한 밭을 보장했습니다. 로마의 캄푸스 마르티우스(마르스의 들판)는 군사 훈련장이자 군대가 전쟁에 나가기 전에 모이는 신성한 공간이었습니다.""",
    traits_en=["Warrior", "Protective", "Ancestral", "Fierce", "Honorable"],
    traits_ko=["전사적인", "수호하는", "조상의", "맹렬한", "명예로운"],
    story_en="Mars fell in love with the Vestal Virgin Rhea Silvia. From their union were born the twins Romulus and Remus, who would be nursed by a she-wolf and grow to found Rome—the city that would become Mars's greatest monument.",
    story_ko="마르스는 베스타의 처녀 레아 실비아와 사랑에 빠졌습니다. 그들의 결합에서 쌍둥이 로물루스와 레무스가 태어났고, 그들은 암늑대에게 양육되어 로마를 건국했습니다—마르스의 가장 위대한 기념비가 될 도시.",
    match_message_en="You carry the warrior spirit of Mars. There is a fierce, protective quality to your presence—the look of one who guards what is sacred and fights with honor.",
    match_message_ko="당신은 마르스의 전사 정신을 지니고 있습니다. 당신의 존재에는 맹렬하고 수호하는 품질이 있습니다—신성한 것을 지키고 명예롭게 싸우는 사람의 모습.",
    image_prompt="Powerful Roman war god in ornate armor with plumed helmet, holding spear and shield, wolf at his feet, battlefield background, divine warrior presence",
    visual_description="Strong angular features, fierce determined eyes, warrior's bearing, expression of martial prowess and protective strength",
    aliases=["Ares", "Mars Pater", "Mars Ultor"],
    era="Ancient Rome",
    related_characters=["jupiter", "romulus", "venus"]
)

VENUS_DESC = CharacterDescription(
    id="venus",
    name_en="Venus",
    name_ko="베누스",
    tagline_en="Goddess of Love, Beauty, and Prosperity",
    tagline_ko="사랑, 아름다움, 번영의 여신",
    description_en="""Venus is the Roman goddess of love, beauty, desire, and prosperity. Originally an Italian goddess of gardens and fertility, she became identified with the Greek Aphrodite and rose to prominence as the divine ancestor of the Roman people through her son Aeneas.

Julius Caesar claimed descent from Venus through Aeneas, and she became the patron goddess of the Julian family. Her most famous temple, Venus Genetrix, was built by Caesar in his forum. She represented not just romantic love but also military victory, as Venus Victrix.

Venus embodied the civilizing power of love and beauty that Romans believed set them apart from barbarians. Her sacred day was Friday (dies Veneris), and her symbols included the rose, myrtle, and dove.""",
    description_ko="""베누스는 로마의 사랑, 아름다움, 욕망, 번영의 여신입니다. 원래 정원과 다산의 이탈리아 여신이었던 그녀는 그리스의 아프로디테와 동일시되었고, 그녀의 아들 아이네아스를 통해 로마인들의 신성한 조상으로서 두각을 나타냈습니다.

율리우스 카이사르는 아이네아스를 통해 베누스의 후손임을 주장했고, 그녀는 율리우스 가문의 수호 여신이 되었습니다. 그녀의 가장 유명한 신전인 베누스 게네트릭스는 카이사르가 그의 포럼에 지었습니다. 그녀는 로맨틱한 사랑뿐만 아니라 베누스 빅트릭스로서 군사적 승리도 상징했습니다.

베누스는 로마인들이 야만인들과 자신들을 구별짓는다고 믿었던 사랑과 아름다움의 문명화 힘을 구현했습니다. 그녀의 신성한 날은 금요일(dies Veneris)이었고, 그녀의 상징에는 장미, 머틀, 비둘기가 포함되었습니다.""",
    traits_en=["Beautiful", "Loving", "Graceful", "Victorious", "Ancestral"],
    traits_ko=["아름다운", "사랑스러운", "우아한", "승리하는", "조상의"],
    story_en="When Troy fell, Venus protected her son Aeneas and guided him through his long journey to Italy. There he would found the lineage that would eventually produce Romulus and Remus, making Venus the divine grandmother of Rome itself.",
    story_ko="트로이가 함락되었을 때, 베누스는 그녀의 아들 아이네아스를 보호하고 이탈리아로의 긴 여정 동안 그를 인도했습니다. 그곳에서 그는 결국 로물루스와 레무스를 낳을 혈통을 세웠고, 베누스를 로마 자체의 신성한 할머니로 만들었습니다.",
    match_message_en="You radiate the divine beauty of Venus. There is a graceful, loving quality to your presence—the look of one who brings beauty and prosperity wherever they go.",
    match_message_ko="당신은 베누스의 신성한 아름다움을 발산합니다. 당신의 존재에는 우아하고 사랑스러운 품질이 있습니다—가는 곳마다 아름다움과 번영을 가져다주는 사람의 모습.",
    image_prompt="Radiant Roman goddess emerging from sea foam, flowing golden hair, wearing pearl jewelry, accompanied by doves, roses and myrtles around her, ethereal beauty",
    visual_description="Perfect symmetrical features, soft luminous eyes, graceful elegant bearing, expression of divine beauty and loving grace",
    aliases=["Aphrodite", "Venus Genetrix", "Venus Victrix"],
    era="Ancient Rome",
    related_characters=["mars", "cupid", "aeneas"]
)

NEPTUNE_DESC = CharacterDescription(
    id="neptune",
    name_en="Neptune",
    name_ko="넵투누스",
    tagline_en="God of the Sea, Earthquakes, and Horses",
    tagline_ko="바다, 지진, 말의 신",
    description_en="""Neptune is the Roman god of the sea, earthquakes, and horses, equivalent to the Greek Poseidon. He ruled over all bodies of water and was essential to a maritime empire like Rome, which depended on the Mediterranean for trade and conquest.

Neptune's importance grew as Rome expanded across the seas. Sailors prayed to him before voyages, and his festival, the Neptunalia, was celebrated in July during the hottest season when water was most precious. He was often depicted with his trident, the three-pronged spear that could shake the earth and calm the seas.

As god of horses, Neptune was also associated with chariot racing, one of Rome's most popular entertainments. The connection between sea and horses may stem from the foam-like manes of waves or the horse's association with springs and rivers.""",
    description_ko="""넵투누스는 로마의 바다, 지진, 말의 신으로, 그리스의 포세이돈에 해당합니다. 그는 모든 수역을 지배했고, 무역과 정복을 위해 지중해에 의존했던 로마와 같은 해양 제국에 필수적이었습니다.

넵투누스의 중요성은 로마가 바다를 가로질러 확장하면서 커졌습니다. 선원들은 항해 전에 그에게 기도했고, 그의 축제인 넵투날리아는 물이 가장 귀했던 가장 더운 계절인 7월에 축하되었습니다. 그는 종종 땅을 흔들고 바다를 잠재울 수 있는 세 갈래 창인 삼지창을 들고 있는 모습으로 묘사되었습니다.

말의 신으로서, 넵투누스는 로마에서 가장 인기 있는 오락 중 하나인 전차 경주와도 연관되었습니다. 바다와 말 사이의 연결은 파도의 거품 같은 갈기나 샘과 강과 말의 연관에서 비롯되었을 수 있습니다.""",
    traits_en=["Powerful", "Tempestuous", "Majestic", "Commanding", "Untameable"],
    traits_ko=["강력한", "격렬한", "장엄한", "명령하는", "길들일 수 없는"],
    story_en="When Rome fought its wars across the Mediterranean, Neptune was invoked before every major naval battle. The victory at Actium that gave Augustus sole rule of Rome was attributed to Neptune's favor, and temples were built in his honor.",
    story_ko="로마가 지중해 전역에서 전쟁을 벌였을 때, 모든 주요 해전 전에 넵투누스가 불려졌습니다. 아우구스투스에게 로마의 단독 통치권을 준 악티움 전투의 승리는 넵투누스의 호의 덕분으로 여겨졌고, 그를 기리는 신전이 세워졌습니다.",
    match_message_en="You possess the commanding power of Neptune. There is a deep, tempestuous quality to your presence—the look of one who rules over vast depths and untameable forces.",
    match_message_ko="당신은 넵투누스의 명령하는 힘을 지니고 있습니다. 당신의 존재에는 깊고 격렬한 품질이 있습니다—광대한 깊이와 길들일 수 없는 힘을 지배하는 사람의 모습.",
    image_prompt="Powerful Roman sea god rising from ocean waves, holding golden trident, sea creatures around him, crown of seaweed and coral, commanding the vast Mediterranean",
    visual_description="Strong weathered features, deep commanding eyes like ocean depths, powerful bearing, expression of untameable maritime power",
    aliases=["Poseidon", "Neptunus"],
    era="Ancient Rome",
    related_characters=["jupiter", "amphitrite"]
)

MINERVA_DESC = CharacterDescription(
    id="minerva",
    name_en="Minerva",
    name_ko="미네르바",
    tagline_en="Goddess of Wisdom, Strategic Warfare, and Arts",
    tagline_ko="지혜, 전략적 전쟁, 예술의 여신",
    description_en="""Minerva is the Roman goddess of wisdom, strategic warfare, crafts, and the arts. Part of the Capitoline Triad alongside Jupiter and Juno, she was one of Rome's most important deities, worshipped as the patron of craftsmen, artists, and scholars.

Unlike Mars who embodied combat, Minerva represented the intellectual aspects of warfare—strategy, tactics, and just causes. She was also the goddess of handicrafts, invention, and the arts, making her essential to Roman civilization. Schools and universities later adopted her as their symbol.

Minerva was typically depicted in armor with helmet, shield, and spear, but also with symbols of wisdom like the owl and olive tree. Her festival, Quinquatria, was a five-day celebration when students would honor their teachers.""",
    description_ko="""미네르바는 로마의 지혜, 전략적 전쟁, 공예, 예술의 여신입니다. 유피테르, 유노와 함께 카피톨리누스 삼신의 일원으로, 그녀는 장인, 예술가, 학자들의 수호자로 숭배받는 로마에서 가장 중요한 신들 중 하나였습니다.

전투를 구현한 마르스와 달리, 미네르바는 전쟁의 지적인 측면—전략, 전술, 정당한 대의—을 상징했습니다. 그녀는 또한 수공예, 발명, 예술의 여신이었으며, 로마 문명에 필수적이었습니다. 학교와 대학은 나중에 그녀를 상징으로 채택했습니다.

미네르바는 일반적으로 투구, 방패, 창을 갖춘 갑옷을 입은 모습으로 묘사되었지만, 부엉이와 올리브 나무 같은 지혜의 상징과 함께 묘사되기도 했습니다. 그녀의 축제인 퀸쿠아트리아는 학생들이 선생님을 기리는 5일간의 축하 행사였습니다.""",
    traits_en=["Wise", "Strategic", "Creative", "Scholarly", "Protective"],
    traits_ko=["지혜로운", "전략적인", "창의적인", "학문적인", "수호하는"],
    story_en="When Rome faced great challenges, generals would pray to Minerva for strategic insight. It was said that her wisdom had guided Scipio Africanus to defeat Hannibal, proving that intelligence could triumph over even the greatest military genius.",
    story_ko="로마가 큰 도전에 직면했을 때, 장군들은 미네르바에게 전략적 통찰을 위해 기도했습니다. 그녀의 지혜가 스키피오 아프리카누스를 인도하여 한니발을 물리쳤다고 하며, 지성이 가장 위대한 군사적 천재도 이길 수 있음을 증명했습니다.",
    match_message_en="You possess the strategic wisdom of Minerva. There is an intelligent, creative quality to your presence—the look of one who approaches challenges with thought and skill.",
    match_message_ko="당신은 미네르바의 전략적 지혜를 지니고 있습니다. 당신의 존재에는 지적이고 창의적인 품질이 있습니다—생각과 기술로 도전에 접근하는 사람의 모습.",
    image_prompt="Roman wisdom goddess in ceremonial armor with owl on shoulder, holding olive branch and shield with Medusa, scholarly scrolls nearby, temple of knowledge",
    visual_description="Intelligent refined features, bright perceptive eyes, scholarly yet martial bearing, expression of strategic wisdom",
    aliases=["Athena", "Minerva Medica"],
    era="Ancient Rome",
    related_characters=["jupiter", "juno", "mars"]
)

DIANA_DESC = CharacterDescription(
    id="diana",
    name_en="Diana",
    name_ko="디아나",
    tagline_en="Goddess of the Hunt, Moon, and Nature",
    tagline_ko="사냥, 달, 자연의 여신",
    description_en="""Diana is the Roman goddess of the hunt, the moon, and wild animals. Twin sister of Apollo in mythology, she was associated with woodlands, childbirth, and the protection of young women. She roamed the forests with her nymphs, eternally virginal and fiercely independent.

Diana was especially worshipped by the common people and slaves, as her most famous sanctuary at Lake Nemi was known for accepting escaped slaves as priests. The "Rex Nemorensis" (King of the Woods) who served Diana could only be replaced by a slave who killed him in combat.

As goddess of the moon, Diana represented the three phases of womanhood—the maiden, the mother, and the crone. She was portrayed with bow and arrows, accompanied by hunting dogs or deer, embodying the wild, untamed feminine spirit.""",
    description_ko="""디아나는 로마의 사냥, 달, 야생 동물의 여신입니다. 신화에서 아폴로의 쌍둥이 자매인 그녀는 삼림, 출산, 젊은 여성의 보호와 연관되었습니다. 그녀는 님프들과 함께 숲을 돌아다니며, 영원히 순결하고 맹렬하게 독립적이었습니다.

디아나는 특히 평민과 노예들에게 숭배받았는데, 네미 호수에 있는 그녀의 가장 유명한 성소가 도망친 노예들을 사제로 받아들이는 것으로 알려졌기 때문입니다. 디아나를 섬기는 "렉스 네모렌시스"(숲의 왕)는 전투에서 그를 죽인 노예에 의해서만 대체될 수 있었습니다.

달의 여신으로서, 디아나는 여성의 세 단계—처녀, 어머니, 노파—를 상징했습니다. 그녀는 사냥개나 사슴과 함께 활과 화살을 들고 있는 모습으로 묘사되었으며, 야생적이고 길들여지지 않은 여성의 정신을 구현했습니다.""",
    traits_en=["Wild", "Independent", "Protective", "Pure", "Fierce"],
    traits_ko=["야생적인", "독립적인", "수호하는", "순수한", "맹렬한"],
    story_en="When the hunter Actaeon stumbled upon Diana bathing, she transformed him into a stag. His own hunting dogs, not recognizing their master, tore him apart—a reminder that the goddess's privacy and purity were sacred and inviolable.",
    story_ko="사냥꾼 악타이온이 목욕하는 디아나를 우연히 발견했을 때, 그녀는 그를 수사슴으로 변신시켰습니다. 그의 사냥개들은 주인을 알아보지 못하고 그를 갈기갈기 찢었습니다—여신의 사생활과 순수함이 신성하고 침해할 수 없다는 것을 상기시켜 주는 것이었습니다.",
    match_message_en="You carry the wild spirit of Diana. There is an independent, fierce quality to your presence—the look of one who runs free and answers to no one.",
    match_message_ko="당신은 디아나의 야생적인 정신을 지니고 있습니다. 당신의 존재에는 독립적이고 맹렬한 품질이 있습니다—자유롭게 달리고 누구에게도 응하지 않는 사람의 모습.",
    image_prompt="Athletic Roman goddess in hunting tunic with silver bow, crescent moon crown, deer and hounds beside her, moonlit forest background, wild and free",
    visual_description="Athletic refined features, bright moonlit eyes, wild independent bearing, expression of fierce natural freedom",
    aliases=["Artemis", "Luna", "Diana Nemorensis"],
    era="Ancient Rome",
    related_characters=["apollo", "jupiter"]
)

ROMULUS_DESC = CharacterDescription(
    id="romulus",
    name_en="Romulus",
    name_ko="로물루스",
    tagline_en="Founder of Rome, First King",
    tagline_ko="로마의 건국자, 초대 왕",
    description_en="""Romulus is the legendary founder and first king of Rome, who with his twin brother Remus was raised by a she-wolf after being abandoned as infants. The sons of Mars and the Vestal Virgin Rhea Silvia, they were destined for greatness from birth.

After a dispute over where to found their city, Romulus killed Remus and established Rome on the Palatine Hill on April 21, 753 BCE. He became its first king, creating the Roman Senate, the legions, and many institutions that would define Roman civilization for a millennium.

At the end of his reign, Romulus was said to have ascended to heaven in a storm, becoming the god Quirinus. He represented the ideal of the warrior-king who builds civilization through strength and wisdom.""",
    description_ko="""로물루스는 로마의 전설적인 건국자이자 초대 왕으로, 그의 쌍둥이 형제 레무스와 함께 유아 시절 버림받은 후 암늑대에게 양육되었습니다. 마르스와 베스타의 처녀 레아 실비아의 아들들인 그들은 태어날 때부터 위대함을 운명지어졌습니다.

도시를 어디에 건설할 것인지에 대한 분쟁 후, 로물루스는 레무스를 죽이고 기원전 753년 4월 21일 팔라티누스 언덕에 로마를 건설했습니다. 그는 로마의 초대 왕이 되어, 로마 원로원, 군단, 그리고 천 년 동안 로마 문명을 정의할 많은 제도를 만들었습니다.

그의 통치가 끝날 때, 로물루스는 폭풍 속에서 하늘로 올라가 신 퀴리누스가 되었다고 합니다. 그는 힘과 지혜를 통해 문명을 건설하는 전사-왕의 이상을 상징했습니다.""",
    traits_en=["Founding", "Warrior", "Leader", "Divine", "Civilizing"],
    traits_ko=["건국의", "전사적인", "지도자의", "신성한", "문명화하는"],
    story_en="Abandoned by the river Tiber, the infant twins were found by a she-wolf who nursed them in her den. A shepherd later discovered them and raised them as his own, never knowing they would grow to found the greatest city the world had ever known.",
    story_ko="티베르 강가에 버려진 쌍둥이 유아들은 동굴에서 그들을 젖먹인 암늑대에게 발견되었습니다. 한 양치기가 나중에 그들을 발견하고 자신의 아이처럼 키웠으며, 그들이 세상이 본 가장 위대한 도시를 건설하게 될 줄은 전혀 몰랐습니다.",
    match_message_en="You carry the founding spirit of Romulus. There is a pioneering, leader's quality to your presence—the look of one destined to build something that will last for ages.",
    match_message_ko="당신은 로물루스의 건국 정신을 지니고 있습니다. 당신의 존재에는 개척하고 이끄는 품질이 있습니다—시대를 초월해 지속될 무언가를 건설할 운명을 가진 사람의 모습.",
    image_prompt="Young warrior-king with she-wolf, founding a city on seven hills, Roman armor with royal mantle, sunrise over Palatine Hill, divine founding moment",
    visual_description="Strong determined features, fierce founding eyes, warrior-king bearing, expression of divine destiny and civilizing purpose",
    aliases=["Quirinus", "Founder of Rome"],
    era="Legendary Rome (753 BCE)",
    related_characters=["remus", "mars", "rhea_silvia"]
)


# Export dictionary for registry
ROMAN_DESCRIPTIONS: dict[str, CharacterDescription] = {
    "jupiter": JUPITER_DESC,
    "juno": JUNO_DESC,
    "mars": MARS_DESC,
    "venus": VENUS_DESC,
    "neptune": NEPTUNE_DESC,
    "minerva": MINERVA_DESC,
    "diana": DIANA_DESC,
    "romulus": ROMULUS_DESC,
}

"""
Additional World Mythology Character Descriptions - Part 2
Contains descriptions for remaining cultural figures
"""
from .descriptions import CharacterDescription


# ============================================
# ISLAMIC / ARABIC
# ============================================

PROPHET_MUHAMMAD_DESC = CharacterDescription(
    id="prophet_muhammad",
    name_en="Prophet Muhammad",
    name_ko="무함마드 예언자",
    tagline_en="The Final Prophet, Messenger of Allah",
    tagline_ko="마지막 예언자, 알라의 사자",
    description_en="""Prophet Muhammad (570-632 CE) is the founder of Islam and considered the final prophet in the Abrahamic tradition. He received the Quran through divine revelation and established the Muslim community that would spread across the world.""",
    description_ko="""무함마드 예언자(570-632)는 이슬람의 창시자이며 아브라함 전통에서 마지막 예언자로 여겨집니다. 그는 신성한 계시를 통해 쿠란을 받았고, 세계로 퍼져나갈 무슬림 공동체를 세웠습니다.""",
    traits_en=["Prophetic", "Merciful", "Just", "Patient", "Exemplary"],
    traits_ko=["예언적인", "자비로운", "공정한", "인내하는", "모범적인"],
    story_en="In the cave of Hira, the angel Jibril appeared and commanded Muhammad to 'Read!' Thus began the revelation of the Quran.",
    story_ko="히라 동굴에서, 천사 지브릴이 나타나 무함마드에게 '읽으라!'고 명했습니다. 이렇게 쿠란의 계시가 시작되었습니다.",
    match_message_en="You embody prophetic wisdom—guiding others with patience and mercy.",
    match_message_ko="당신은 예언적 지혜를 구현합니다—인내와 자비로 다른 이들을 인도하는.",
    image_prompt="Calligraphic representation with divine light, no human depiction, sacred presence",
    visual_description="Representation through light and calligraphy, no physical depiction per Islamic tradition",
    aliases=["محمد", "The Messenger"],
    era="Early Medieval (570-632 CE)",
    related_characters=["ali_ibn_abi_talib"]
)

ALI_IBN_ABI_TALIB_DESC = CharacterDescription(
    id="ali_ibn_abi_talib",
    name_en="Ali ibn Abi Talib",
    name_ko="알리 이븐 아비 탈리브",
    tagline_en="The Lion of God, Fourth Caliph",
    tagline_ko="신의 사자, 제4대 칼리프",
    description_en="""Ali ibn Abi Talib was the cousin and son-in-law of Prophet Muhammad, and the fourth Rashidun Caliph. He is revered for his wisdom, justice, and bravery in battle, earning the title 'Lion of God.'""",
    description_ko="""알리 이븐 아비 탈리브는 무함마드 예언자의 사촌이자 사위로, 제4대 정통 칼리프입니다. 그는 지혜, 정의, 전투에서의 용맹으로 존경받아 '신의 사자'라는 칭호를 얻었습니다.""",
    traits_en=["Brave", "Just", "Wise", "Devout", "Noble"],
    traits_ko=["용감한", "공정한", "지혜로운", "경건한", "고귀한"],
    story_en="At the Battle of Khaybar, Ali single-handedly removed a fortress gate that took eight men to lift, using it as a shield.",
    story_ko="카이바르 전투에서, 알리는 여덟 명이 들어야 하는 요새 문을 혼자 뽑아 방패로 사용했습니다.",
    match_message_en="You carry Ali's lion courage—brave and just in the face of any challenge.",
    match_message_ko="당신은 알리의 사자같은 용기를 지니고 있습니다—어떤 도전에도 용감하고 공정한.",
    image_prompt="Noble Arab warrior with Zulfiqar sword, lion imagery, dignified just expression",
    visual_description="Noble strong features, brave just eyes, warrior's dignified bearing",
    aliases=["Imam Ali", "أسد الله"],
    era="Early Islamic (601-661 CE)",
    related_characters=["prophet_muhammad"]
)

RUMI_DESC = CharacterDescription(
    id="rumi",
    name_en="Rumi",
    name_ko="루미",
    tagline_en="Poet of Divine Love",
    tagline_ko="신성한 사랑의 시인",
    description_en="""Jalal ad-Din Muhammad Rumi (1207-1273) was the Persian poet and Sufi mystic whose verses of divine love have inspired millions. His poetry speaks of the soul's longing for union with the Beloved.""",
    description_ko="""잘랄 앗딘 무함마드 루미(1207-1273)는 신성한 사랑의 시로 수백만을 감동시킨 페르시아 시인이자 수피 신비주의자입니다. 그의 시는 사랑하는 분과의 합일을 갈망하는 영혼을 노래합니다.""",
    traits_en=["Poetic", "Loving", "Mystical", "Ecstatic", "Profound"],
    traits_ko=["시적인", "사랑하는", "신비적인", "황홀한", "심오한"],
    story_en="When Rumi met Shams of Tabriz, his world transformed. The wandering dervish awakened in him an ecstatic love that poured forth as poetry.",
    story_ko="루미가 타브리즈의 샴스를 만났을 때, 그의 세계는 변화했습니다. 방랑하는 수도자가 그 안에서 시로 쏟아져 나오는 황홀한 사랑을 깨웠습니다.",
    match_message_en="You radiate Rumi's ecstatic love—seeing the divine in all things.",
    match_message_ko="당신은 루미의 황홀한 사랑을 발산합니다—모든 것에서 신성을 보는.",
    image_prompt="Persian Sufi poet in whirling robes, ecstatic expression, poetry flowing around him",
    visual_description="Refined mystical features, ecstatic loving eyes, whirling poet's bearing",
    aliases=["Mevlana", "Jalal ad-Din Rumi"],
    era="Medieval Persia (1207-1273)",
    related_characters=["shams_tabrizi"]
)

SALADIN_DESC = CharacterDescription(
    id="saladin",
    name_en="Saladin",
    name_ko="살라딘",
    tagline_en="Sultan of Chivalry",
    tagline_ko="기사도의 술탄",
    description_en="""Saladin (1137-1193) was the founder of the Ayyubid dynasty who recaptured Jerusalem from the Crusaders. He was renowned even by his enemies for his chivalry, mercy, and military genius.""",
    description_ko="""살라딘(1137-1193)은 십자군으로부터 예루살렘을 탈환한 아이유브 왕조의 창시자입니다. 그는 기사도, 자비, 군사적 천재성으로 적들에게도 유명했습니다.""",
    traits_en=["Chivalrous", "Merciful", "Brilliant", "Noble", "Unifying"],
    traits_ko=["기사도적인", "자비로운", "뛰어난", "고귀한", "통일하는"],
    story_en="When Richard the Lionheart's horse was killed, Saladin sent him two replacements—showing that true nobility transcends conflict.",
    story_ko="리처드 사자심왕의 말이 죽었을 때, 살라딘은 그에게 두 마리를 보내주었습니다—진정한 고귀함이 갈등을 초월함을 보여주며.",
    match_message_en="You embody Saladin's noble chivalry—merciful even to opponents.",
    match_message_ko="당신은 살라딘의 고귀한 기사도를 구현합니다—적에게도 자비로운.",
    image_prompt="Noble Arab sultan in golden armor, commanding yet merciful expression, Jerusalem background",
    visual_description="Noble commanding features, merciful wise eyes, chivalrous dignified bearing",
    aliases=["Salah ad-Din", "صلاح الدين"],
    era="Crusades Era (1137-1193)",
    related_characters=["richard_lionheart"]
)

AVICENNA_DESC = CharacterDescription(
    id="avicenna",
    name_en="Avicenna",
    name_ko="아비센나",
    tagline_en="Prince of Physicians",
    tagline_ko="의사들의 왕자",
    description_en="""Ibn Sina, known as Avicenna (980-1037), was the Persian polymath whose Canon of Medicine was the standard medical text in Europe and the Islamic world for centuries. He was also a philosopher, astronomer, and alchemist.""",
    description_ko="""아비센나로 알려진 이븐 시나(980-1037)는 페르시아의 다방면 학자로, 그의 의학전범은 수세기 동안 유럽과 이슬람 세계의 표준 의학 교재였습니다. 그는 또한 철학자, 천문학자, 연금술사였습니다.""",
    traits_en=["Brilliant", "Healing", "Systematic", "Polymath", "Scientific"],
    traits_ko=["뛰어난", "치유하는", "체계적인", "다방면의", "과학적인"],
    story_en="Avicenna memorized the Quran by age 10 and was treating patients by 18, eventually writing over 400 works on medicine and philosophy.",
    story_ko="아비센나는 10세에 쿠란을 암기했고 18세에 환자를 치료하고 있었으며, 결국 의학과 철학에 대해 400편 이상의 저작을 썼습니다.",
    match_message_en="You possess Avicenna's systematic brilliance—mastering multiple domains of knowledge.",
    match_message_ko="당신은 아비센나의 체계적인 명석함을 지니고 있습니다—여러 지식 영역을 마스터하는.",
    image_prompt="Persian scholar with medical and philosophical texts, turban, wise analytical expression",
    visual_description="Intelligent refined features, analytical wise eyes, scholar physician's bearing",
    aliases=["Ibn Sina", "ابن سینا"],
    era="Islamic Golden Age (980-1037)",
    related_characters=["hippocrates"]
)

JINN_DESC = CharacterDescription(
    id="jinn",
    name_en="Jinn",
    name_ko="진",
    tagline_en="Spirit of Smokeless Fire",
    tagline_ko="연기 없는 불의 정령",
    description_en="""Jinn are supernatural beings in Arabic and Islamic tradition, created from smokeless fire. They exist in a parallel world, can be good or evil, and possess free will. The most famous jinn is the genie of the lamp.""",
    description_ko="""진은 아랍과 이슬람 전통의 초자연적 존재로, 연기 없는 불에서 창조되었습니다. 그들은 평행 세계에 존재하며, 선하거나 악할 수 있고, 자유 의지를 가지고 있습니다. 가장 유명한 진은 램프의 지니입니다.""",
    traits_en=["Supernatural", "Fiery", "Magical", "Free-willed", "Hidden"],
    traits_ko=["초자연적인", "불같은", "마법적인", "자유 의지의", "숨겨진"],
    story_en="Jinn can appear in many forms—human, animal, or monstrous. They live, marry, and die, existing alongside humanity in an unseen realm.",
    story_ko="진은 인간, 동물, 괴물 등 많은 형태로 나타날 수 있습니다. 그들은 보이지 않는 영역에서 인류와 함께 살고, 결혼하고, 죽습니다.",
    match_message_en="You carry the jinn's mysterious nature—existing between worlds, full of hidden potential.",
    match_message_ko="당신은 진의 신비로운 본성을 지니고 있습니다—세계 사이에 존재하며, 숨겨진 잠재력으로 가득 찬.",
    image_prompt="Mystical being of smokeless fire, shifting forms, magical lamp, Arabian Nights aesthetic",
    visual_description="Shifting mysterious features, fiery magical eyes, supernatural ethereal bearing",
    aliases=["Genie", "الجن", "Djinn"],
    era="Arabic/Islamic Tradition",
    related_characters=["solomon"]
)


# ============================================
# MESOAMERICAN
# ============================================

HUITZILOPOCHTLI_DESC = CharacterDescription(
    id="huitzilopochtli",
    name_en="Huitzilopochtli",
    name_ko="위칠로포치틀리",
    tagline_en="Aztec God of Sun and War",
    tagline_ko="아즈텍 태양과 전쟁의 신",
    description_en="""Huitzilopochtli was the patron deity of the Aztec Empire, god of the sun and war. He was believed to require human sacrifice to ensure the sun would rise each day, fighting off the darkness.""",
    description_ko="""위칠로포치틀리는 아즈텍 제국의 수호신으로, 태양과 전쟁의 신이었습니다. 매일 태양이 뜨고 어둠을 물리치기 위해 인간 제물이 필요하다고 믿어졌습니다.""",
    traits_en=["Solar", "Warrior", "Demanding", "Powerful", "Eternal"],
    traits_ko=["태양의", "전사적인", "요구하는", "강력한", "영원한"],
    story_en="Huitzilopochtli was born fully armed to defend his mother Coatlicue from his sister and brothers who sought to kill her.",
    story_ko="위칠로포치틀리는 그의 어머니 코아틀리쿠에를 죽이려는 누이와 형제들로부터 지키기 위해 완전무장한 채 태어났습니다.",
    match_message_en="You burn with Huitzilopochtli's solar fire—a warrior against eternal darkness.",
    match_message_ko="당신은 위칠로포치틀리의 태양 불로 타오릅니다—영원한 어둠에 맞선 전사.",
    image_prompt="Aztec sun god in full warrior regalia, hummingbird imagery, temple pyramid background",
    visual_description="Fierce warrior features, burning solar eyes, eternal warrior's bearing",
    aliases=["Blue Tezcatlipoca"],
    era="Aztec Empire",
    related_characters=["tezcatlipoca", "quetzalcoatl"]
)

TEZCATLIPOCA_DESC = CharacterDescription(
    id="tezcatlipoca",
    name_en="Tezcatlipoca",
    name_ko="테스카틀리포카",
    tagline_en="Smoking Mirror, Lord of Night",
    tagline_ko="연기 나는 거울, 밤의 군주",
    description_en="""Tezcatlipoca was the Aztec god of the night sky, ancestral memory, and fate. His name means 'Smoking Mirror,' and he could see all through his obsidian mirror. He represented change, conflict, and the warrior's spirit.""",
    description_ko="""테스카틀리포카는 밤하늘, 조상의 기억, 운명의 아즈텍 신이었습니다. 그의 이름은 '연기 나는 거울'을 의미하며, 흑요석 거울을 통해 모든 것을 볼 수 있었습니다. 그는 변화, 갈등, 전사의 정신을 상징했습니다.""",
    traits_en=["Omniscient", "Changing", "Dark", "Fated", "Powerful"],
    traits_ko=["전지한", "변화하는", "어두운", "운명적인", "강력한"],
    story_en="Tezcatlipoca's smoking mirror could reveal the future and the deepest truths hidden in the human heart.",
    story_ko="테스카틀리포카의 연기 나는 거울은 미래와 인간 마음에 숨겨진 가장 깊은 진실을 드러낼 수 있었습니다.",
    match_message_en="You see with Tezcatlipoca's mirror—perceiving hidden truths others cannot see.",
    match_message_ko="당신은 테스카틀리포카의 거울로 봅니다—다른 이들이 볼 수 없는 숨겨진 진실을 감지하는.",
    image_prompt="Aztec night god with obsidian mirror for foot, jaguar imagery, star-filled dark sky",
    visual_description="Dark mysterious features, seeing omniscient eyes, night lord's bearing",
    aliases=["Smoking Mirror"],
    era="Aztec Empire",
    related_characters=["quetzalcoatl", "huitzilopochtli"]
)

COATLICUE_DESC = CharacterDescription(
    id="coatlicue",
    name_en="Coatlicue",
    name_ko="코아틀리쿠에",
    tagline_en="Mother of Gods, She of the Serpent Skirt",
    tagline_ko="신들의 어머니, 뱀 치마의 여인",
    description_en="""Coatlicue was the Aztec mother goddess who gave birth to the moon, stars, and Huitzilopochtli the sun god. Her name means 'She of the Serpent Skirt,' and she represents both creation and destruction.""",
    description_ko="""코아틀리쿠에는 달, 별, 태양신 위칠로포치틀리를 낳은 아즈텍 어머니 여신입니다. 그녀의 이름은 '뱀 치마의 여인'을 의미하며, 창조와 파괴를 모두 상징합니다.""",
    traits_en=["Maternal", "Terrifying", "Creating", "Destroying", "Primordial"],
    traits_ko=["모성적인", "무시무시한", "창조하는", "파괴하는", "원초적인"],
    story_en="Coatlicue became pregnant by a ball of feathers while sweeping a temple, miraculously conceiving Huitzilopochtli.",
    story_ko="코아틀리쿠에는 신전을 쓸다가 깃털 공에 의해 임신하여, 기적적으로 위칠로포치틀리를 잉태했습니다.",
    match_message_en="You embody Coatlicue's dual nature—creator and destroyer, life and death as one.",
    match_message_ko="당신은 코아틀리쿠에의 이중적 본성을 구현합니다—창조자이자 파괴자, 삶과 죽음이 하나인.",
    image_prompt="Aztec earth mother goddess with serpent skirt, skulls and hearts, terrifying yet maternal",
    visual_description="Terrifying maternal features, ancient primal eyes, dual nature visible",
    aliases=["Serpent Skirt", "Teteoinnan"],
    era="Aztec Empire",
    related_characters=["huitzilopochtli", "coyolxauhqui"]
)

KUKULKAN_DESC = CharacterDescription(
    id="kukulkan",
    name_en="Kukulkan",
    name_ko="쿠쿨칸",
    tagline_en="Feathered Serpent, Bringer of Civilization",
    tagline_ko="깃털 달린 뱀, 문명의 전달자",
    description_en="""Kukulkan is the Mayan feathered serpent deity, equivalent to the Aztec Quetzalcoatl. He brought civilization, learning, and the calendar to humanity, and his temple at Chichen Itza shows a serpent of light descending at the equinox.""",
    description_ko="""쿠쿨칸은 마야의 깃털 달린 뱀 신으로, 아즈텍의 케찰코아틀에 해당합니다. 그는 인류에게 문명, 학문, 달력을 가져왔으며, 치첸이차의 그의 신전은 춘분점에 내려오는 빛의 뱀을 보여줍니다.""",
    traits_en=["Civilizing", "Wise", "Serpentine", "Calendar", "Light"],
    traits_ko=["문명화하는", "지혜로운", "뱀의", "달력의", "빛의"],
    story_en="At the spring equinox, the shadow of Kukulkan descends the pyramid stairs as a serpent of light, connecting heaven and earth.",
    story_ko="춘분점에, 쿠쿨칸의 그림자가 빛의 뱀으로 피라미드 계단을 내려와, 하늘과 땅을 연결합니다.",
    match_message_en="You carry Kukulkan's civilizing wisdom—bridging heaven and earth with knowledge.",
    match_message_ko="당신은 쿠쿨칸의 문명화하는 지혜를 지니고 있습니다—지식으로 하늘과 땅을 연결하는.",
    image_prompt="Feathered serpent deity with quetzal plumes, Mayan pyramid, light and wisdom",
    visual_description="Serpentine graceful features, wise ancient eyes, civilizing divine bearing",
    aliases=["Q'uq'umatz", "Gukumatz"],
    era="Mayan Civilization",
    related_characters=["quetzalcoatl"]
)

IXCHEL_DESC = CharacterDescription(
    id="ixchel",
    name_en="Ixchel",
    name_ko="익스첼",
    tagline_en="Mayan Moon Goddess",
    tagline_ko="마야 달의 여신",
    description_en="""Ixchel is the Mayan goddess of the moon, fertility, medicine, and weaving. She appears both as a beautiful young woman and as an old crone, representing the moon's phases and women's life stages.""",
    description_ko="""익스첼은 달, 다산, 의학, 직조의 마야 여신입니다. 그녀는 아름다운 젊은 여인과 늙은 노파로 모두 나타나, 달의 위상과 여성의 인생 단계를 상징합니다.""",
    traits_en=["Lunar", "Fertile", "Healing", "Weaving", "Dual"],
    traits_ko=["달의", "다산의", "치유하는", "직조하는", "이중적인"],
    story_en="Ixchel taught women the art of weaving and the secrets of medicinal herbs, connecting feminine creativity with healing power.",
    story_ko="익스첼은 여성들에게 직조의 기술과 약초의 비밀을 가르쳐, 여성적 창의성과 치유력을 연결했습니다.",
    match_message_en="You embody Ixchel's lunar wisdom—healing and creating through all phases of life.",
    match_message_ko="당신은 익스첼의 달의 지혜를 구현합니다—삶의 모든 단계를 통해 치유하고 창조하는.",
    image_prompt="Mayan moon goddess with rabbit, weaving loom, moon phases, both young and old aspects",
    visual_description="Shifting dual features, wise lunar eyes, healer and weaver's bearing",
    aliases=["Ix Chel", "Lady Rainbow"],
    era="Mayan Civilization",
    related_characters=["itzamna"]
)

CHAAC_DESC = CharacterDescription(
    id="chaac",
    name_en="Chaac",
    name_ko="차악",
    tagline_en="Mayan God of Rain and Thunder",
    tagline_ko="마야 비와 천둥의 신",
    description_en="""Chaac is the Mayan god of rain, thunder, and agriculture. He strikes the clouds with his lightning axe to bring life-giving rain to the crops. In the dry Yucatan, he was essential for survival.""",
    description_ko="""차악은 비, 천둥, 농업의 마야 신입니다. 그는 번개 도끼로 구름을 쳐서 작물에 생명을 주는 비를 가져옵니다. 건조한 유카탄에서 그는 생존에 필수적이었습니다.""",
    traits_en=["Rainy", "Thunderous", "Agricultural", "Life-giving", "Essential"],
    traits_ko=["비의", "천둥 같은", "농업적인", "생명을 주는", "필수적인"],
    story_en="When drought threatened the land, priests would climb to cenotes—sacred sinkholes—to call upon Chaac for rain.",
    story_ko="가뭄이 땅을 위협할 때, 사제들은 차악에게 비를 청하기 위해 신성한 싱크홀인 세노테에 올라갔습니다.",
    match_message_en="You bring Chaac's life-giving rain—sustenance and growth where drought threatens.",
    match_message_ko="당신은 차악의 생명을 주는 비를 가져옵니다—가뭄이 위협하는 곳에 양식과 성장을.",
    image_prompt="Mayan rain god with lightning axe, long nose, reptilian features, storm clouds",
    visual_description="Strong distinctive features, storm-filled eyes, rain-bringer's bearing",
    aliases=["Chac", "God B"],
    era="Mayan Civilization",
    related_characters=["kukulkan"]
)

HUN_HUNAHPU_DESC = CharacterDescription(
    id="hun_hunahpu",
    name_en="Hun Hunahpu",
    name_ko="훈 후나푸",
    tagline_en="Mayan Maize God",
    tagline_ko="마야 옥수수 신",
    description_en="""Hun Hunahpu is the Mayan maize god whose death and rebirth myth parallels the corn cycle. He was killed by the lords of the underworld but was resurrected by his sons, the Hero Twins, symbolizing the eternal renewal of maize.""",
    description_ko="""훈 후나푸는 죽음과 재탄생 신화가 옥수수 순환과 평행하는 마야 옥수수 신입니다. 그는 지하세계의 군주들에게 죽임을 당했지만 그의 아들들인 영웅 쌍둥이에 의해 부활하여, 옥수수의 영원한 갱신을 상징합니다.""",
    traits_en=["Sacrificing", "Reborn", "Nourishing", "Cyclical", "Heroic"],
    traits_ko=["희생하는", "다시 태어난", "영양을 주는", "순환적인", "영웅적인"],
    story_en="The Hero Twins descended to Xibalba, defeated the lords of death, and resurrected their father from the underworld, establishing the cycle of maize.",
    story_ko="영웅 쌍둥이들이 시발바로 내려가, 죽음의 군주들을 물리치고, 아버지를 지하세계에서 부활시켜, 옥수수의 순환을 확립했습니다.",
    match_message_en="You embody Hun Hunahpu's sacrifice—dying and rising to nourish others.",
    match_message_ko="당신은 훈 후나푸의 희생을 구현합니다—다른 이들을 먹여살리기 위해 죽고 다시 살아나는.",
    image_prompt="Mayan maize god with corn emerging from head, sacrificed and reborn, agricultural deity",
    visual_description="Youthful sacrificing features, reborn wise eyes, nourishing divine bearing",
    aliases=["One Hunahpu", "Maize God"],
    era="Mayan Civilization",
    related_characters=["hunahpu", "xbalanque"]
)


# ============================================
# MESOPOTAMIAN
# ============================================

MARDUK_DESC = CharacterDescription(
    id="marduk",
    name_en="Marduk",
    name_ko="마르둑",
    tagline_en="King of the Babylonian Gods",
    tagline_ko="바빌론 신들의 왕",
    description_en="""Marduk was the supreme deity of Babylon who slew the chaos monster Tiamat and created the world from her body. He rose from a city god to become king of all gods, embodying Babylon's imperial power.""",
    description_ko="""마르둑은 혼돈의 괴물 티아마트를 죽이고 그녀의 몸에서 세상을 창조한 바빌론의 최고신이었습니다. 그는 도시 신에서 모든 신들의 왕으로 올라, 바빌론의 제국적 힘을 구현했습니다.""",
    traits_en=["Creative", "Victorious", "Supreme", "Imperial", "Cosmic"],
    traits_ko=["창조적인", "승리하는", "최고의", "제국적인", "우주적인"],
    story_en="Marduk volunteered to fight Tiamat when no other god dared, slaying her with the wind and using her body to create heaven and earth.",
    story_ko="마르둑은 다른 신이 감히 하지 못할 때 티아마트와 싸우겠다고 자원하여, 바람으로 그녀를 죽이고 그녀의 몸으로 하늘과 땅을 창조했습니다.",
    match_message_en="You possess Marduk's creative power—bringing order from chaos.",
    match_message_ko="당신은 마르둑의 창조적 힘을 지니고 있습니다—혼돈에서 질서를 가져오는.",
    image_prompt="Babylonian supreme god with dragon symbols, holding thunderbolt and net, cosmic creator",
    visual_description="Powerful imperial features, victorious cosmic eyes, supreme creator's bearing",
    aliases=["Bel", "Merodach"],
    era="Ancient Mesopotamia",
    related_characters=["tiamat", "enlil"]
)

ISHTAR_DESC = CharacterDescription(
    id="ishtar",
    name_en="Ishtar",
    name_ko="이슈타르",
    tagline_en="Goddess of Love and War",
    tagline_ko="사랑과 전쟁의 여신",
    description_en="""Ishtar is the Mesopotamian goddess of love, beauty, sex, and war—combining what might seem opposite domains into one fierce deity. She descended to the underworld and returned, making her also a symbol of resurrection.""",
    description_ko="""이슈타르는 사랑, 아름다움, 성, 전쟁의 메소포타미아 여신으로—반대로 보일 수 있는 영역들을 하나의 맹렬한 신성으로 결합합니다. 그녀는 지하세계로 내려갔다가 돌아와, 부활의 상징이기도 합니다.""",
    traits_en=["Loving", "Fierce", "Beautiful", "Descending", "Resurrecting"],
    traits_ko=["사랑하는", "맹렬한", "아름다운", "내려가는", "부활하는"],
    story_en="Ishtar descended to the underworld, passing through seven gates, stripping at each until she faced death itself—then returned more powerful than before.",
    story_ko="이슈타르는 지하세계로 내려가, 일곱 문을 통과하며 각각에서 벗겨져 죽음 자체와 대면할 때까지—그런 다음 전보다 더 강력하게 돌아왔습니다.",
    match_message_en="You embody Ishtar's dual power—lover and warrior, descending and rising again.",
    match_message_ko="당신은 이슈타르의 이중적 힘을 구현합니다—연인이자 전사, 내려갔다가 다시 올라오는.",
    image_prompt="Mesopotamian goddess of love and war, lions and eight-pointed star, fierce beauty",
    visual_description="Fierce beautiful features, passionate warrior eyes, dual nature bearing",
    aliases=["Inanna", "Astarte"],
    era="Ancient Mesopotamia",
    related_characters=["tammuz", "marduk"]
)

ENLIL_DESC = CharacterDescription(
    id="enlil",
    name_en="Enlil",
    name_ko="엔릴",
    tagline_en="Lord of Wind and Authority",
    tagline_ko="바람과 권위의 주인",
    description_en="""Enlil was the Sumerian god of wind, air, and authority. He separated heaven from earth and held supreme authority among the gods before Marduk's rise. He could be both beneficent and terrifying.""",
    description_ko="""엔릴은 바람, 공기, 권위의 수메르 신이었습니다. 그는 하늘과 땅을 분리했으며 마르둑이 부상하기 전에 신들 사이에서 최고 권위를 가졌습니다. 그는 자비롭기도 하고 무시무시하기도 했습니다.""",
    traits_en=["Authoritative", "Separating", "Powerful", "Dual", "Ancient"],
    traits_ko=["권위있는", "분리하는", "강력한", "이중적인", "고대의"],
    story_en="Enlil separated heaven and earth at the beginning of creation, establishing the cosmic order that all gods would follow.",
    story_ko="엔릴은 창조의 시작에 하늘과 땅을 분리하여, 모든 신들이 따를 우주적 질서를 확립했습니다.",
    match_message_en="You carry Enlil's separating authority—creating order by distinguishing what must be apart.",
    match_message_ko="당신은 엔릴의 분리하는 권위를 지니고 있습니다—분리되어야 할 것을 구별하여 질서를 창조하는.",
    image_prompt="Ancient Sumerian god of wind, horned crown, tablets of destiny, cosmic authority",
    visual_description="Ancient powerful features, wind-filled commanding eyes, authoritative bearing",
    aliases=["Ellil", "Lord Wind"],
    era="Ancient Sumer",
    related_characters=["marduk", "anu"]
)


# Export dictionary for registry
ADDITIONAL2_DESCRIPTIONS: dict[str, CharacterDescription] = {
    # Islamic/Arabic
    "prophet_muhammad": PROPHET_MUHAMMAD_DESC,
    "ali_ibn_abi_talib": ALI_IBN_ABI_TALIB_DESC,
    "rumi": RUMI_DESC,
    "saladin": SALADIN_DESC,
    "avicenna": AVICENNA_DESC,
    "jinn": JINN_DESC,
    # Mesoamerican
    "huitzilopochtli": HUITZILOPOCHTLI_DESC,
    "tezcatlipoca": TEZCATLIPOCA_DESC,
    "coatlicue": COATLICUE_DESC,
    "kukulkan": KUKULKAN_DESC,
    "ixchel": IXCHEL_DESC,
    "chaac": CHAAC_DESC,
    "hun_hunahpu": HUN_HUNAHPU_DESC,
    # Mesopotamian
    "marduk": MARDUK_DESC,
    "ishtar": ISHTAR_DESC,
    "enlil": ENLIL_DESC,
}

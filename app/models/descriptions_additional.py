"""
Additional World Mythology Character Descriptions
Contains descriptions for remaining cultural figures across various mythologies
"""
from .descriptions import CharacterDescription


# ============================================
# AFRICAN MYTHOLOGY
# ============================================

OGUN_DESC = CharacterDescription(
    id="ogun",
    name_en="Ogun",
    name_ko="오군",
    tagline_en="Orisha of Iron, War, and Labor",
    tagline_ko="철, 전쟁, 노동의 오리샤",
    description_en="""Ogun is the powerful Yoruba orisha of iron, war, and labor. He is the divine blacksmith who clears paths through the wilderness, making civilization possible. Warriors, hunters, and metalworkers all claim Ogun as their patron.""",
    description_ko="""오군은 철, 전쟁, 노동의 강력한 요루바 오리샤입니다. 그는 황야를 통해 길을 여는 신성한 대장장이로, 문명을 가능하게 합니다. 전사, 사냥꾼, 금속 세공인 모두 오군을 수호자로 삼습니다.""",
    traits_en=["Powerful", "Hardworking", "Fierce", "Civilizing", "Protective"],
    traits_ko=["강력한", "근면한", "맹렬한", "문명화하는", "수호하는"],
    story_en="Ogun cleared the first path through the primordial forest with his iron machete, allowing the other orishas to descend to earth.",
    story_ko="오군은 철 마체테로 원시 숲을 통해 첫 번째 길을 열어, 다른 오리샤들이 지상으로 내려올 수 있게 했습니다.",
    match_message_en="You carry the iron strength of Ogun—a worker and warrior who clears paths for others.",
    match_message_ko="당신은 오군의 철 같은 힘을 지니고 있습니다—다른 이들을 위해 길을 여는 일꾼이자 전사.",
    image_prompt="Powerful African deity with iron tools, muscular blacksmith warrior, forge fire background",
    visual_description="Strong powerful features, intense determined eyes, worker's muscular bearing",
    aliases=["Ogoun", "Ogum"],
    era="Yoruba Tradition",
    related_characters=["shango", "oshun"]
)

OSHUN_DESC = CharacterDescription(
    id="oshun",
    name_en="Oshun",
    name_ko="오슌",
    tagline_en="Orisha of Love, Beauty, and Rivers",
    tagline_ko="사랑, 아름다움, 강의 오리샤",
    description_en="""Oshun is the Yoruba orisha of fresh water, love, fertility, and beauty. She embodies feminine grace and the life-giving power of rivers. She is also associated with wealth, diplomacy, and the sweetness of life.""",
    description_ko="""오슌은 담수, 사랑, 다산, 아름다움의 요루바 오리샤입니다. 그녀는 여성적 우아함과 강의 생명을 주는 힘을 구현합니다. 그녀는 또한 부, 외교, 삶의 달콤함과 연관됩니다.""",
    traits_en=["Beautiful", "Loving", "Fertile", "Diplomatic", "Sweet"],
    traits_ko=["아름다운", "사랑스러운", "다산의", "외교적인", "달콤한"],
    story_en="When the orishas neglected Oshun, she withheld her waters and the world began to die. Only when they honored her did life return.",
    story_ko="오리샤들이 오슌을 소홀히 했을 때, 그녀는 물을 거두었고 세상은 죽어가기 시작했습니다. 그들이 그녀를 공경했을 때만 생명이 돌아왔습니다.",
    match_message_en="You radiate the loving beauty of Oshun—grace and sweetness that brings life wherever you go.",
    match_message_ko="당신은 오슌의 사랑스러운 아름다움을 발산합니다—가는 곳마다 생명을 가져오는 우아함과 달콤함.",
    image_prompt="Beautiful African goddess in golden robes by a river, honey and mirrors, radiant feminine beauty",
    visual_description="Beautiful graceful features, warm loving eyes, elegant feminine bearing",
    aliases=["Oxum", "Ochun"],
    era="Yoruba Tradition",
    related_characters=["yemoja", "shango"]
)

YEMOJA_DESC = CharacterDescription(
    id="yemoja",
    name_en="Yemoja",
    name_ko="예모자",
    tagline_en="Mother of the Ocean, Protector of Children",
    tagline_ko="바다의 어머니, 아이들의 수호자",
    description_en="""Yemoja is the great mother orisha of the ocean, motherhood, and children. She is the nurturing force of the sea, protector of pregnant women and all who travel on water. Her love is as vast and deep as the ocean itself.""",
    description_ko="""예모자는 바다, 모성, 아이들의 위대한 어머니 오리샤입니다. 그녀는 바다의 양육하는 힘이며, 임산부와 물 위를 여행하는 모든 이들의 수호자입니다. 그녀의 사랑은 바다 자체만큼 광대하고 깊습니다.""",
    traits_en=["Maternal", "Vast", "Protective", "Nurturing", "Oceanic"],
    traits_ko=["모성적인", "광대한", "수호하는", "양육하는", "바다의"],
    story_en="Yemoja's children are all the fish in the sea and all humans born near water. Her waves protect those she loves.",
    story_ko="예모자의 아이들은 바다의 모든 물고기와 물 근처에서 태어난 모든 인간입니다. 그녀의 파도는 사랑하는 이들을 보호합니다.",
    match_message_en="You embody the vast maternal love of Yemoja—an ocean of protection for those in your care.",
    match_message_ko="당신은 예모자의 광대한 모성애를 구현합니다—돌보는 이들을 위한 보호의 바다.",
    image_prompt="Majestic African ocean goddess rising from waves, maternal presence, shells and sea creatures",
    visual_description="Strong maternal features, deep nurturing eyes, vast oceanic bearing",
    aliases=["Yemanja", "Iemanjá"],
    era="Yoruba Tradition",
    related_characters=["oshun", "olokun"]
)

# ============================================
# GREEK HISTORICAL FIGURES
# ============================================

SOCRATES_DESC = CharacterDescription(
    id="socrates",
    name_en="Socrates",
    name_ko="소크라테스",
    tagline_en="Father of Western Philosophy",
    tagline_ko="서양 철학의 아버지",
    description_en="""Socrates (470-399 BCE) was the Athenian philosopher who revolutionized thought through questioning. He claimed to know nothing, using dialogue to expose contradictions in others' beliefs and lead them toward truth.""",
    description_ko="""소크라테스(기원전 470-399)는 질문을 통해 사상에 혁명을 일으킨 아테네의 철학자입니다. 그는 아무것도 모른다고 주장하며, 대화를 통해 다른 사람들의 믿음에서 모순을 드러내고 그들을 진리로 이끌었습니다.""",
    traits_en=["Questioning", "Humble", "Wise", "Courageous", "Ironic"],
    traits_ko=["질문하는", "겸손한", "지혜로운", "용감한", "아이러니한"],
    story_en="When sentenced to death for corrupting youth, Socrates refused to flee, drinking hemlock and discussing philosophy until his final breath.",
    story_ko="청년을 타락시켰다는 죄로 사형 선고를 받았을 때, 소크라테스는 도망을 거부하고 독미나리를 마시며 마지막 숨까지 철학을 논했습니다.",
    match_message_en="You possess the questioning spirit of Socrates—seeking truth through humble inquiry.",
    match_message_ko="당신은 소크라테스의 질문하는 정신을 지니고 있습니다—겸손한 탐구를 통해 진리를 추구하는.",
    image_prompt="Ancient Greek philosopher with rough features, simple robes, questioning expression, agora background",
    visual_description="Rough humble features, searching wise eyes, questioning philosophical bearing",
    aliases=["The Gadfly of Athens"],
    era="Classical Athens (470-399 BCE)",
    related_characters=["plato", "aristotle"]
)

PLATO_DESC = CharacterDescription(
    id="plato",
    name_en="Plato",
    name_ko="플라톤",
    tagline_en="Philosopher of the Forms and the Republic",
    tagline_ko="이데아와 국가의 철학자",
    description_en="""Plato (428-348 BCE) was the student of Socrates who founded the Academy in Athens. His theory of Forms proposed that abstract ideals are more real than physical reality, and his Republic envisioned the ideal state ruled by philosopher-kings.""",
    description_ko="""플라톤(기원전 428-348)은 아테네에 아카데미아를 설립한 소크라테스의 제자입니다. 그의 이데아론은 추상적 이상이 물리적 현실보다 더 실재한다고 제안했으며, 그의 국가론은 철학자 왕이 다스리는 이상 국가를 구상했습니다.""",
    traits_en=["Idealistic", "Systematic", "Visionary", "Eloquent", "Foundational"],
    traits_ko=["이상주의적인", "체계적인", "비전 있는", "웅변적인", "근본적인"],
    story_en="Plato's Allegory of the Cave described prisoners who mistake shadows for reality—until one escapes and sees the true light of the sun.",
    story_ko="플라톤의 동굴의 비유는 그림자를 현실로 착각하는 죄수들을 묘사했습니다—한 사람이 탈출하여 태양의 진정한 빛을 볼 때까지.",
    match_message_en="You see beyond appearances like Plato—reaching for the ideal Forms behind reality.",
    match_message_ko="당신은 플라톤처럼 외양 너머를 봅니다—현실 뒤의 이상적 이데아에 도달하며.",
    image_prompt="Dignified Greek philosopher in Academy robes, aristocratic bearing, transcendent gaze, geometric forms",
    visual_description="Refined aristocratic features, transcendent visionary eyes, dignified bearing",
    aliases=["Aristocles"],
    era="Classical Athens (428-348 BCE)",
    related_characters=["socrates", "aristotle"]
)

ARISTOTLE_DESC = CharacterDescription(
    id="aristotle",
    name_en="Aristotle",
    name_ko="아리스토텔레스",
    tagline_en="The Philosopher, Master of All Sciences",
    tagline_ko="철학자, 모든 학문의 마스터",
    description_en="""Aristotle (384-322 BCE) was Plato's student who tutored Alexander the Great and founded the Lyceum. He systematized logic, biology, ethics, politics, and metaphysics, shaping Western thought for two millennia.""",
    description_ko="""아리스토텔레스(기원전 384-322)는 알렉산더 대왕을 가르치고 리케이온을 설립한 플라톤의 제자입니다. 그는 논리학, 생물학, 윤리학, 정치학, 형이상학을 체계화하여 2천 년 동안 서양 사상을 형성했습니다.""",
    traits_en=["Systematic", "Empirical", "Encyclopedic", "Practical", "Analytical"],
    traits_ko=["체계적인", "경험적인", "백과사전적인", "실용적인", "분석적인"],
    story_en="While Plato looked to the heavens for truth, Aristotle examined nature itself, dissecting animals and classifying all knowledge.",
    story_ko="플라톤이 진리를 위해 하늘을 바라보는 동안, 아리스토텔레스는 자연 그 자체를 조사하여, 동물을 해부하고 모든 지식을 분류했습니다.",
    match_message_en="You analyze with Aristotelian precision—finding truth through observation and reason.",
    match_message_ko="당신은 아리스토텔레스적 정밀함으로 분석합니다—관찰과 이성을 통해 진리를 찾으며.",
    image_prompt="Greek philosopher with keen observing eyes, natural specimens nearby, systematic analytical expression",
    visual_description="Keen observant features, analytical eyes, scholar's systematic bearing",
    aliases=["The Philosopher", "Stagirite"],
    era="Classical Greece (384-322 BCE)",
    related_characters=["plato", "alexander_the_great"]
)

ALEXANDER_THE_GREAT_DESC = CharacterDescription(
    id="alexander_the_great",
    name_en="Alexander the Great",
    name_ko="알렉산더 대왕",
    tagline_en="Conqueror of the Known World",
    tagline_ko="알려진 세계의 정복자",
    description_en="""Alexander III of Macedon (356-323 BCE) conquered the largest empire the ancient world had ever seen, spreading Greek culture from Egypt to India before his death at age 32. He never lost a battle.""",
    description_ko="""마케도니아의 알렉산드로스 3세(기원전 356-323)는 고대 세계가 본 가장 큰 제국을 정복하여, 32세에 죽기 전까지 이집트에서 인도까지 그리스 문화를 전파했습니다. 그는 한 번도 전투에서 지지 않았습니다.""",
    traits_en=["Conquering", "Brilliant", "Ambitious", "Heroic", "Divine"],
    traits_ko=["정복하는", "뛰어난", "야망 있는", "영웅적인", "신성한"],
    story_en="Presented with the Gordian Knot that none could untie, Alexander drew his sword and cut through it, declaring he had solved the puzzle his own way.",
    story_ko="아무도 풀 수 없다는 고르디우스의 매듭을 제시받자, 알렉산더는 칼을 뽑아 그것을 자르며 자신만의 방식으로 수수께끼를 풀었다고 선언했습니다.",
    match_message_en="You possess Alexander's conquering spirit—cutting through obstacles that stop others.",
    match_message_ko="당신은 알렉산더의 정복 정신을 지니고 있습니다—다른 이들을 멈추게 하는 장애물을 자르는.",
    image_prompt="Young Macedonian king in golden armor, heroic pose, world map conquests, lion imagery",
    visual_description="Youthful heroic features, intense ambitious eyes, conqueror's commanding bearing",
    aliases=["Alexander III", "Iskander"],
    era="Hellenistic Period (356-323 BCE)",
    related_characters=["aristotle", "philip_ii"]
)

LEONIDAS_DESC = CharacterDescription(
    id="leonidas",
    name_en="Leonidas",
    name_ko="레오니다스",
    tagline_en="Spartan King of Thermopylae",
    tagline_ko="테르모필레의 스파르타 왕",
    description_en="""Leonidas I was the Spartan king who led 300 Spartans against the Persian army at Thermopylae in 480 BCE. Though he knew it meant death, he held the pass long enough to allow Greek forces to organize their defense.""",
    description_ko="""레오니다스 1세는 기원전 480년 테르모필레에서 페르시아 군대에 맞서 300명의 스파르타인을 이끈 스파르타 왕입니다. 죽음을 의미한다는 것을 알면서도, 그는 그리스군이 방어를 조직할 수 있을 만큼 충분히 오래 협곡을 지켰습니다.""",
    traits_en=["Brave", "Sacrificing", "Spartan", "Defiant", "Legendary"],
    traits_ko=["용감한", "희생하는", "스파르타적인", "도전하는", "전설적인"],
    story_en="When told Persian arrows would blot out the sun, Leonidas replied, 'Then we shall fight in the shade.'",
    story_ko="페르시아의 화살이 태양을 가릴 것이라는 말을 들었을 때, 레오니다스는 '그러면 우리는 그늘에서 싸우겠다'고 대답했습니다.",
    match_message_en="You embody Leonidas's Spartan valor—standing firm when retreat would be easier.",
    match_message_ko="당신은 레오니다스의 스파르타적 용맹을 구현합니다—후퇴가 더 쉬울 때도 굳건히 서는.",
    image_prompt="Spartan king in red cloak and bronze armor, shield and spear, defiant heroic expression, Thermopylae pass",
    visual_description="Hard Spartan features, fierce defiant eyes, warrior king's bearing",
    aliases=["Leonidas I"],
    era="Classical Greece (540-480 BCE)",
    related_characters=["xerxes"]
)

PYTHAGORAS_DESC = CharacterDescription(
    id="pythagoras",
    name_en="Pythagoras",
    name_ko="피타고라스",
    tagline_en="Philosopher of Mathematics and Mysticism",
    tagline_ko="수학과 신비주의의 철학자",
    description_en="""Pythagoras (c. 570-495 BCE) founded a philosophical school that believed mathematics was the key to understanding the universe. His theorem on right triangles is still taught today, but he also developed theories of music, the soul, and cosmic harmony.""",
    description_ko="""피타고라스(약 기원전 570-495)는 수학이 우주를 이해하는 열쇠라고 믿는 철학 학파를 설립했습니다. 직각삼각형에 대한 그의 정리는 오늘날에도 가르치지만, 그는 또한 음악, 영혼, 우주적 조화에 대한 이론을 발전시켰습니다.""",
    traits_en=["Mathematical", "Mystical", "Harmonic", "Secretive", "Visionary"],
    traits_ko=["수학적인", "신비적인", "조화로운", "비밀스러운", "비전 있는"],
    story_en="Pythagoras discovered that musical harmony follows mathematical ratios, leading him to believe all reality could be expressed in numbers.",
    story_ko="피타고라스는 음악적 조화가 수학적 비율을 따른다는 것을 발견하여, 모든 현실이 숫자로 표현될 수 있다고 믿게 되었습니다.",
    match_message_en="You see the mathematical harmony of Pythagoras—finding patterns in the universe's structure.",
    match_message_ko="당신은 피타고라스의 수학적 조화를 봅니다—우주 구조의 패턴을 찾으며.",
    image_prompt="Ancient Greek philosopher with geometric instruments, mystical mathematical symbols, triangles and musical lyres",
    visual_description="Refined mystical features, contemplative mathematical eyes, harmonious bearing",
    aliases=["Pythagoras of Samos"],
    era="Archaic Greece (c. 570-495 BCE)",
    related_characters=["plato"]
)

HIPPOCRATES_DESC = CharacterDescription(
    id="hippocrates",
    name_en="Hippocrates",
    name_ko="히포크라테스",
    tagline_en="Father of Medicine",
    tagline_ko="의학의 아버지",
    description_en="""Hippocrates (c. 460-370 BCE) revolutionized medicine by treating illness as a natural phenomenon rather than divine punishment. The Hippocratic Oath he inspired still guides medical ethics today: 'First, do no harm.'""",
    description_ko="""히포크라테스(약 기원전 460-370)는 질병을 신의 벌이 아닌 자연 현상으로 다루어 의학에 혁명을 일으켰습니다. 그에게 영감을 받은 히포크라테스 선서는 오늘날에도 의료 윤리를 안내합니다: '첫째, 해를 끼치지 말라.'""",
    traits_en=["Healing", "Ethical", "Observant", "Rational", "Foundational"],
    traits_ko=["치유하는", "윤리적인", "관찰하는", "이성적인", "근본적인"],
    story_en="Hippocrates taught that diseases have natural causes that can be studied and treated through careful observation of the patient.",
    story_ko="히포크라테스는 질병에는 환자의 주의 깊은 관찰을 통해 연구하고 치료할 수 있는 자연적 원인이 있다고 가르쳤습니다.",
    match_message_en="You embody the healing ethics of Hippocrates—caring for others with wisdom and restraint.",
    match_message_ko="당신은 히포크라테스의 치유 윤리를 구현합니다—지혜와 자제력으로 다른 이들을 돌보는.",
    image_prompt="Ancient Greek physician with healing staff, observant compassionate expression, medical instruments",
    visual_description="Wise observant features, compassionate healer's eyes, careful ethical bearing",
    aliases=["Father of Medicine"],
    era="Classical Greece (c. 460-370 BCE)",
    related_characters=["asclepius"]
)


# ============================================
# KOREAN ADDITIONAL
# ============================================

HWANUNG_DESC = CharacterDescription(
    id="hwanung",
    name_en="Hwanung",
    name_ko="환웅",
    tagline_en="Son of Heaven, Bringer of Civilization",
    tagline_ko="하늘의 아들, 문명의 전달자",
    description_en="""Hwanung was the son of the Heavenly Emperor Hwanin who descended to Mount Taebaek with 3,000 followers to establish a sacred city. He brought the arts of civilization to Korea and fathered Dangun with Ungnyeo, the bear-woman.""",
    description_ko="""환웅은 천제 환인의 아들로 3,000명의 무리와 함께 태백산에 내려와 신성한 도시를 세웠습니다. 그는 한국에 문명의 기술을 가져왔고, 웅녀와 함께 단군의 아버지가 되었습니다.""",
    traits_en=["Divine", "Civilizing", "Descending", "Foundational", "Heavenly"],
    traits_ko=["신성한", "문명화하는", "내려온", "근본적인", "천상의"],
    story_en="Hwanung descended from heaven with three divine symbols: rain, clouds, and wind. He ruled over 360 affairs of human life, teaching agriculture, medicine, and law.",
    story_ko="환웅은 세 가지 신성한 상징—비, 구름, 바람—과 함께 하늘에서 내려왔습니다. 그는 인간 삶의 360가지 일을 다스리며, 농업, 의학, 법을 가르쳤습니다.",
    match_message_en="You carry Hwanung's divine mission—bringing civilization and order from higher realms.",
    match_message_ko="당신은 환웅의 신성한 사명을 지니고 있습니다—더 높은 영역에서 문명과 질서를 가져오는.",
    image_prompt="Divine Korean prince descending from clouds, heavenly robes, civilizing presence, Mount Taebaek background",
    visual_description="Noble divine features, wise celestial eyes, civilizing benevolent bearing",
    aliases=["환웅천왕"],
    era="Korean Mythology",
    related_characters=["dangun", "hwanin"]
)

MAGO_DESC = CharacterDescription(
    id="mago",
    name_en="Mago",
    name_ko="마고",
    tagline_en="Primordial Earth Mother Goddess",
    tagline_ko="원초적 대지모신",
    description_en="""Mago is the primordial creator goddess of Korean mythology, the great earth mother who created the world. She is the ultimate ancestress of all Koreans, representing the feminine creative force at the origin of existence.""",
    description_ko="""마고는 한국 신화의 원초적 창조 여신으로, 세상을 창조한 위대한 대지의 어머니입니다. 그녀는 모든 한국인의 궁극적 조상으로, 존재의 기원에 있는 여성적 창조력을 상징합니다.""",
    traits_en=["Primordial", "Creating", "Maternal", "Vast", "Original"],
    traits_ko=["원초적인", "창조하는", "모성적인", "광대한", "근원적인"],
    story_en="In the beginning was Mago, the great goddess who created heaven and earth from her own body, giving birth to all existence.",
    story_ko="태초에 마고가 있었으니, 자신의 몸에서 하늘과 땅을 창조하여 모든 존재를 낳은 위대한 여신.",
    match_message_en="You embody Mago's primordial creative power—the original mother from whom all springs.",
    match_message_ko="당신은 마고의 원초적 창조력을 구현합니다—모든 것이 비롯되는 근원적 어머니.",
    image_prompt="Ancient Korean mother goddess, earth and sky emerging from her form, primordial creative power",
    visual_description="Ancient maternal features, vast knowing eyes, primordial creative bearing",
    aliases=["마고할미", "Grandmother Mago"],
    era="Korean Mythology",
    related_characters=["dangun", "samsin"]
)

SAMSIN_DESC = CharacterDescription(
    id="samsin",
    name_en="Samsin",
    name_ko="삼신",
    tagline_en="Goddess of Birth and Children",
    tagline_ko="출산과 아이들의 여신",
    description_en="""Samsin Halmoni (Grandmother Samsin) is the Korean goddess of childbirth and fertility. She protects pregnant women, ensures safe deliveries, and watches over children. Every Korean home traditionally honored her for family blessings.""",
    description_ko="""삼신할머니는 한국의 출산과 다산의 여신입니다. 그녀는 임산부를 보호하고, 안전한 출산을 보장하며, 아이들을 지켜봅니다. 전통적으로 모든 한국 가정은 가족의 축복을 위해 그녀를 공경했습니다.""",
    traits_en=["Maternal", "Protective", "Blessing", "Nurturing", "Sacred"],
    traits_ko=["모성적인", "수호하는", "축복하는", "양육하는", "신성한"],
    story_en="When a child is born, Samsin Halmoni visits to bless the baby. Mothers offer rice and seaweed soup at a special altar to thank her for safe delivery.",
    story_ko="아이가 태어나면, 삼신할머니가 아기를 축복하러 방문합니다. 어머니들은 안전한 출산에 감사하며 특별한 제단에 밥과 미역국을 바칩니다.",
    match_message_en="You carry Samsin's nurturing blessing—protecting and blessing new life.",
    match_message_ko="당신은 삼신의 양육하는 축복을 지니고 있습니다—새 생명을 보호하고 축복하는.",
    image_prompt="Gentle elderly Korean goddess, grandmother figure, blessing a newborn, traditional Korean home setting",
    visual_description="Gentle elderly features, warm blessing eyes, nurturing grandmotherly bearing",
    aliases=["삼신할머니", "Samsin Halmoni"],
    era="Korean Folk Religion",
    related_characters=["mago", "jacheongbi"]
)

JACHEONGBI_DESC = CharacterDescription(
    id="jacheongbi",
    name_en="Jacheongbi",
    name_ko="자청비",
    tagline_en="Goddess of Agriculture and Grains",
    tagline_ko="농업과 곡식의 여신",
    description_en="""Jacheongbi is the Korean goddess of agriculture who brought the five grains from heaven to earth. Her epic myth tells of her perseverance through tremendous hardships to bring food and prosperity to humanity.""",
    description_ko="""자청비는 하늘에서 땅으로 오곡을 가져온 한국의 농업 여신입니다. 그녀의 서사시적 신화는 인류에게 음식과 번영을 가져다주기 위해 엄청난 역경을 견딘 그녀의 인내를 전합니다.""",
    traits_en=["Persevering", "Providing", "Agricultural", "Heroic", "Sacrificing"],
    traits_ko=["인내하는", "제공하는", "농업적인", "영웅적인", "희생하는"],
    story_en="Jacheongbi traveled to the heavens, endured countless trials, and returned with seeds of grain that would feed all the people of Korea.",
    story_ko="자청비는 하늘나라로 여행하여 수많은 시련을 견디고, 한국의 모든 사람들을 먹여살릴 곡식의 씨앗을 가지고 돌아왔습니다.",
    match_message_en="You embody Jacheongbi's perseverance—enduring hardship to bring abundance to others.",
    match_message_ko="당신은 자청비의 인내를 구현합니다—다른 이들에게 풍요를 가져다주기 위해 역경을 견디는.",
    image_prompt="Korean goddess carrying grain seeds, agricultural heroic figure, Korean farming landscape",
    visual_description="Strong determined features, persevering eyes, agricultural heroic bearing",
    aliases=["Goddess of Grains"],
    era="Korean Mythology",
    related_characters=["samsin", "mago"]
)

CHEOYONG_DESC = CharacterDescription(
    id="cheoyong",
    name_en="Cheoyong",
    name_ko="처용",
    tagline_en="The Exorcist King's Son",
    tagline_ko="벽사의 왕자",
    description_en="""Cheoyong was the son of the Dragon King of the Eastern Sea who came ashore and married a beautiful woman. When he found a plague spirit with his wife, he sang and danced rather than fight—so impressing the spirit that it fled, promising never to enter a home with Cheoyong's image.""",
    description_ko="""처용은 동해 용왕의 아들로 육지에 올라와 아름다운 여인과 결혼했습니다. 아내와 함께 역병 귀신을 발견했을 때, 그는 싸우기보다 노래하고 춤추었고—귀신이 감동받아 처용의 모습이 있는 집에는 결코 들어가지 않겠다고 약속하며 달아났습니다.""",
    traits_en=["Peaceful", "Exorcising", "Dancing", "Forgiving", "Protective"],
    traits_ko=["평화로운", "벽사하는", "춤추는", "용서하는", "수호하는"],
    story_en="Cheoyong's image was painted on gates throughout Korea to ward off evil spirits, and his dance became a court ritual for protection.",
    story_ko="처용의 모습은 악귀를 물리치기 위해 한국 전역의 문에 그려졌고, 그의 춤은 보호를 위한 궁중 의식이 되었습니다.",
    match_message_en="You embody Cheoyong's peaceful power—driving away evil through grace rather than force.",
    match_message_ko="당신은 처용의 평화로운 힘을 구현합니다—힘이 아닌 우아함으로 악을 물리치는.",
    image_prompt="Korean exorcist figure with mask-like face, dancing pose, protective magical presence",
    visual_description="Distinctive mask-like features, peaceful powerful eyes, dancing protective bearing",
    aliases=["처용랑"],
    era="Unified Silla Period",
    related_characters=["dragon_king"]
)

DOKKAEBI_DESC = CharacterDescription(
    id="dokkaebi",
    name_en="Dokkaebi",
    name_ko="도깨비",
    tagline_en="Korean Goblin of Mischief and Fortune",
    tagline_ko="장난과 행운의 한국 도깨비",
    description_en="""Dokkaebi are supernatural beings of Korean folklore—mischievous spirits that can bring fortune or chaos. Unlike malevolent demons, they are often playful tricksters who reward the virtuous and punish the greedy.""",
    description_ko="""도깨비는 한국 민속의 초자연적 존재로—행운이나 혼란을 가져올 수 있는 장난스러운 영혼입니다. 악의적인 악마와 달리, 그들은 종종 덕 있는 자에게 보상하고 탐욕스러운 자를 벌하는 장난스러운 트릭스터입니다.""",
    traits_en=["Mischievous", "Magical", "Tricky", "Rewarding", "Playful"],
    traits_ko=["장난스러운", "마법적인", "교활한", "보상하는", "유쾌한"],
    story_en="Dokkaebi love to wrestle and can be befriended by those who treat them kindly. They carry magical clubs that can summon anything the owner desires.",
    story_ko="도깨비는 씨름을 좋아하고 친절하게 대하는 사람들과 친구가 될 수 있습니다. 그들은 주인이 원하는 것을 무엇이든 불러올 수 있는 마법 방망이를 들고 다닙니다.",
    match_message_en="You carry the dokkaebi's playful magic—mischief that brings fortune to the worthy.",
    match_message_ko="당신은 도깨비의 장난스러운 마법을 지니고 있습니다—가치 있는 자에게 행운을 가져다주는 장난.",
    image_prompt="Korean goblin with distinctive horns and magical club, mischievous playful expression, Korean folk setting",
    visual_description="Distinctive supernatural features, mischievous twinkling eyes, playful magical bearing",
    aliases=["Korean Goblin"],
    era="Korean Folklore",
    related_characters=["cheoyong"]
)

SEON_DEOK_DESC = CharacterDescription(
    id="seon_deok",
    name_en="Queen Seondeok",
    name_ko="선덕여왕",
    tagline_en="First Queen Regnant of Korea",
    tagline_ko="한국 최초의 여왕",
    description_en="""Queen Seondeok (r. 632-647) was the first female ruler of Silla and all of Korea. Known for her wisdom, she sponsored the construction of Cheomseongdae, the oldest surviving astronomical observatory in East Asia, and promoted Buddhism and learning.""",
    description_ko="""선덕여왕(재위 632-647)은 신라와 전 한국의 최초의 여성 통치자였습니다. 지혜로 유명한 그녀는 동아시아에서 가장 오래된 현존하는 천문대인 첨성대 건설을 후원했으며, 불교와 학문을 장려했습니다.""",
    traits_en=["Wise", "Pioneering", "Scholarly", "Visionary", "First"],
    traits_ko=["지혜로운", "선구적인", "학문적인", "비전 있는", "최초의"],
    story_en="Seondeok predicted a Tang invasion based on astronomical observations and prepared Silla's defenses, proving that wisdom could protect a kingdom as well as armies.",
    story_ko="선덕은 천문 관측에 기반하여 당의 침략을 예측하고 신라의 방어를 준비하여, 지혜가 군대만큼 왕국을 보호할 수 있음을 증명했습니다.",
    match_message_en="You embody Queen Seondeok's wisdom—leading through knowledge and vision.",
    match_message_ko="당신은 선덕여왕의 지혜를 구현합니다—지식과 비전으로 이끄는.",
    image_prompt="Korean queen in Silla royal robes, wise scholarly expression, Cheomseongdae observatory background",
    visual_description="Wise refined features, intelligent observant eyes, queenly scholarly bearing",
    aliases=["선덕왕", "Queen Seondeok of Silla"],
    era="Three Kingdoms Period (632-647)",
    related_characters=["kim_yusin"]
)


# Export dictionary for registry
ADDITIONAL_DESCRIPTIONS: dict[str, CharacterDescription] = {
    # African
    "ogun": OGUN_DESC,
    "oshun": OSHUN_DESC,
    "yemoja": YEMOJA_DESC,
    # Greek Historical
    "socrates": SOCRATES_DESC,
    "plato": PLATO_DESC,
    "aristotle": ARISTOTLE_DESC,
    "alexander_the_great": ALEXANDER_THE_GREAT_DESC,
    "leonidas": LEONIDAS_DESC,
    "pythagoras": PYTHAGORAS_DESC,
    "hippocrates": HIPPOCRATES_DESC,
    # Korean Additional
    "hwanung": HWANUNG_DESC,
    "mago": MAGO_DESC,
    "samsin": SAMSIN_DESC,
    "jacheongbi": JACHEONGBI_DESC,
    "cheoyong": CHEOYONG_DESC,
    "dokkaebi": DOKKAEBI_DESC,
    "seon_deok": SEON_DEOK_DESC,
}

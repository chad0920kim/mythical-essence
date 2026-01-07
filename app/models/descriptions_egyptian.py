"""
Egyptian Mythology - Additional Character Descriptions
Extends the base descriptions.py with more Egyptian figures to reach 20+
"""
from .descriptions import CharacterDescription


# Additional Egyptian Mythology Figures (to reach 20+)

NEPHTHYS_DESC = CharacterDescription(
    id="nephthys",
    name_en="Nephthys",
    name_ko="네프티스",
    tagline_en="Goddess of Mourning, Protector of the Dead",
    tagline_ko="애도의 여신, 죽은 자의 수호자",
    description_en="""Nephthys is the goddess of mourning, darkness, and protection of the dead. Sister of Isis, Osiris, and Set, she plays a crucial role in funerary rites and the journey of souls to the afterlife.

Though married to Set, Nephthys aided Isis in gathering Osiris's scattered body and performed the first mourning rites. Her protective wings are often depicted sheltering the deceased, guiding them safely through the underworld.

She represents the necessary darkness that accompanies death, the comfort found in mourning, and the protective love that extends even beyond life.""",
    description_ko="""네프티스는 애도, 어둠, 죽은 자 보호의 여신입니다. 이시스, 오시리스, 세트의 자매로, 장례 의식과 영혼이 사후세계로 가는 여정에서 중요한 역할을 합니다.

세트와 결혼했지만, 네프티스는 이시스가 오시리스의 흩어진 몸을 모으는 것을 돕고 최초의 애도 의식을 행했습니다. 그녀의 보호하는 날개는 종종 고인을 감싸며 지하세계를 안전하게 안내하는 모습으로 묘사됩니다.

그녀는 죽음과 함께 오는 필연적인 어둠, 애도에서 발견되는 위안, 그리고 삶을 넘어서까지 확장되는 보호하는 사랑을 대표합니다.""",
    traits_en=["Mourning", "Protective", "Dark", "Sisterly", "Guiding"],
    traits_ko=["애도하는", "보호하는", "어두운", "자매같은", "안내하는"],
    story_en="When Set scattered Osiris's body across Egypt, Nephthys joined her sister Isis in the search. Together they found every piece, and Nephthys's mourning cries were so powerful they helped restore Osiris to a form of life in the underworld.",
    story_ko="세트가 오시리스의 몸을 이집트 전역에 흩어놓았을 때, 네프티스는 자매 이시스와 함께 수색에 나섰습니다. 함께 모든 조각을 찾았고, 네프티스의 애도하는 울음은 너무 강력해서 오시리스가 지하세계에서 삶의 한 형태로 회복되도록 도왔습니다.",
    match_message_en="Your features carry the protective darkness of Nephthys. There is comforting strength in your appearance—the look of one who guides others through their darkest moments with gentle protection.",
    match_message_ko="당신의 이목구비는 네프티스의 보호하는 어둠을 담고 있습니다. 당신의 외모에는 위안을 주는 힘이 있습니다—가장 어두운 순간을 부드러운 보호로 안내하는 사람의 모습.",
    image_prompt="Egyptian goddess with protective winged arms, kneeling in mourning pose, hieroglyphic symbols, dark blue and gold colors, temple at twilight, expression of compassionate grief, ancient Egyptian art style",
    visual_description="Regal sorrowful features, compassionate protective eyes, dark beauty, expression of one who comforts in darkness",
    aliases=["Lady of the Temple", "Friend of the Dead"],
    era="Ancient Egypt",
    related_characters=["isis", "osiris", "set", "anubis"]
)

MA_AT_DESC = CharacterDescription(
    id="maat",
    name_en="Ma'at",
    name_ko="마아트",
    tagline_en="Goddess of Truth, Justice, and Cosmic Order",
    tagline_ko="진실, 정의, 우주 질서의 여신",
    description_en="""Ma'at is the goddess who personifies truth, justice, balance, and cosmic order. She represents the fundamental principle that governs all creation—the harmony that allows existence itself to continue.

Her feather is used in the weighing of the heart ceremony, where the deceased's heart is measured against it. Only hearts lighter than Ma'at's feather may pass into the afterlife; those found wanting are devoured.

Ma'at represents the universal law that transcends even the gods, the principle that right conduct and truth are the foundations of existence.""",
    description_ko="""마아트는 진실, 정의, 균형, 우주 질서를 의인화한 여신입니다. 그녀는 모든 창조를 지배하는 근본 원리—존재 자체가 계속될 수 있게 하는 조화를 대표합니다.

그녀의 깃털은 심장을 재는 의식에서 사용되는데, 고인의 심장이 그것과 비교해 측정됩니다. 마아트의 깃털보다 가벼운 심장만이 사후세계로 갈 수 있고, 부족한 것으로 판명된 것들은 삼켜집니다.

마아트는 신들조차 초월하는 보편적 법칙, 올바른 행동과 진실이 존재의 기초라는 원리를 대표합니다.""",
    traits_en=["Truthful", "Just", "Balanced", "Cosmic", "Measuring"],
    traits_ko=["진실한", "공정한", "균형 잡힌", "우주적인", "측정하는"],
    story_en="In the Hall of Two Truths, Anubis places the heart of the deceased on one side of the scales and Ma'at's feather on the other. If the heart, heavy with sin, outweighs the feather, the monster Ammit devours it. The just heart passes to eternal life.",
    story_ko="두 진실의 전당에서 아누비스가 저울 한쪽에 고인의 심장을, 다른 쪽에 마아트의 깃털을 올려놓습니다. 죄로 무거워진 심장이 깃털보다 무거우면 괴물 아밋이 그것을 삼킵니다. 의로운 심장은 영원한 생명으로 나아갑니다.",
    match_message_en="Your features carry the balanced truth of Ma'at. There is natural justice in your appearance—the look of one who embodies fairness and maintains harmony through right action.",
    match_message_ko="당신의 이목구비는 마아트의 균형 잡힌 진실을 담고 있습니다. 당신의 외모에는 자연스러운 정의가 있습니다—공정함을 구현하고 올바른 행동을 통해 조화를 유지하는 사람의 모습.",
    image_prompt="Serene Egyptian goddess with ostrich feather headdress, holding scales of justice, hieroglyphics of truth and order, golden light of cosmic harmony, expression of impartial divine truth, ancient Egyptian art style",
    visual_description="Serene balanced features, clear just eyes, poised dignified bearing, expression of perfect impartiality and cosmic truth",
    aliases=["Personification of Truth", "Lady of the Judgment Hall"],
    era="Ancient Egypt",
    related_characters=["anubis", "osiris", "thoth", "ra"]
)

SOBEK_DESC = CharacterDescription(
    id="sobek",
    name_en="Sobek",
    name_ko="소베크",
    tagline_en="Crocodile God of Strength and Power",
    tagline_ko="힘과 권력의 악어 신",
    description_en="""Sobek is the crocodile-headed god of strength, power, and fertility. Associated with the life-giving Nile and its dangerous crocodiles, he embodies both the creative and destructive aspects of nature's raw power.

Worshipped in temples where sacred crocodiles lived in pools, Sobek was both feared and revered. He protected pharaohs in battle and was believed to have created the world from the primordial waters.

Sobek represents primal power that can create or destroy, the respect owed to nature's dangerous forces, and the divine authority that rules through strength.""",
    description_ko="""소베크는 힘, 권력, 다산의 악어 머리 신입니다. 생명을 주는 나일강과 그 위험한 악어들과 연관되어, 그는 자연의 순수한 힘의 창조적이고 파괴적인 측면 모두를 구현합니다.

신성한 악어들이 연못에서 살았던 신전에서 숭배받았던 소베크는 두려움과 경외의 대상이었습니다. 그는 전투에서 파라오를 보호했고 태초의 물에서 세계를 창조했다고 믿어졌습니다.

소베크는 창조하거나 파괴할 수 있는 원초적 힘, 자연의 위험한 힘에 대한 존경, 그리고 힘으로 지배하는 신성한 권위를 대표합니다.""",
    traits_en=["Powerful", "Primal", "Protective", "Dangerous", "Fertile"],
    traits_ko=["강력한", "원초적인", "보호하는", "위험한", "다산의"],
    story_en="Sobek emerged from the primordial waters of chaos to create the world. His sweat became the Nile River, bringing life to Egypt. Pharaohs wore crocodile amulets into battle, calling upon Sobek's ferocious protection against their enemies.",
    story_ko="소베크는 혼돈의 태초의 물에서 나와 세계를 창조했습니다. 그의 땀은 나일강이 되어 이집트에 생명을 가져왔습니다. 파라오들은 전투에 악어 부적을 착용하여 적들에 맞서 소베크의 사나운 보호를 불렀습니다.",
    match_message_en="Your features carry the primal power of Sobek. There is fierce strength in your appearance—the look of one who commands respect through sheer force and protects what they value.",
    match_message_ko="당신의 이목구비는 소베크의 원초적인 힘을 담고 있습니다. 당신의 외모에는 사나운 힘이 있습니다—순수한 힘으로 존경을 명령하고 가치 있는 것을 보호하는 사람의 모습.",
    image_prompt="Powerful Egyptian god with crocodile head, muscular human body, holding was-scepter and ankh, Nile River with crocodiles behind, expression of fierce divine power, ancient Egyptian art style",
    visual_description="Powerful fierce features, predatory intense eyes, commanding physical presence, expression of dangerous protective strength",
    aliases=["Lord of the Nile", "The Rager"],
    era="Ancient Egypt",
    related_characters=["ra", "set", "horus", "khnum"]
)

HATHOR_DESC = CharacterDescription(
    id="hathor",
    name_en="Hathor",
    name_ko="하토르",
    tagline_en="Goddess of Love, Beauty, and Joy",
    tagline_ko="사랑, 아름다움, 기쁨의 여신",
    description_en="""Hathor is the goddess of love, beauty, music, dance, and joy. Often depicted with cow's horns cradling a sun disk, she embodies all pleasurable aspects of life and is called the 'Golden One' for her radiant beauty.

She welcomed the dead to the afterlife with drink and food, and was patroness of lovers, artists, and miners seeking turquoise. Yet she also had a fierce aspect—as the Eye of Ra, she once nearly destroyed humanity in her wrath.

Hathor represents the dual nature of feminine divine power—nurturing joy and terrible destruction, life-giving love and consuming rage.""",
    description_ko="""하토르는 사랑, 아름다움, 음악, 춤, 기쁨의 여신입니다. 종종 태양 원반을 감싸는 소 뿔과 함께 묘사되며, 그녀는 삶의 모든 즐거운 측면을 구현하고 빛나는 아름다움으로 '황금빛 존재'라고 불립니다.

그녀는 죽은 자를 음식과 음료로 사후세계에 환영했고, 연인들, 예술가들, 터키석을 찾는 광부들의 수호자였습니다. 그러나 그녀는 또한 사나운 면도 있었습니다—라의 눈으로서, 그녀는 한때 분노로 인류를 거의 멸망시킬 뻔했습니다.

하토르는 여성적 신성한 힘의 이중적 본성을 대표합니다—양육하는 기쁨과 끔찍한 파괴, 생명을 주는 사랑과 소모하는 분노.""",
    traits_en=["Joyful", "Beautiful", "Nurturing", "Fierce", "Golden"],
    traits_ko=["기쁜", "아름다운", "양육하는", "사나운", "황금빛의"],
    story_en="When Ra grew angry at humanity, he sent Hathor as his Eye to punish them. She became Sekhmet and slaughtered humans until the Nile ran red. Ra, regretting his decree, tricked her with beer dyed red like blood. She drank, became peaceful Hathor again, and humanity was saved.",
    story_ko="라가 인류에게 화가 났을 때, 그는 하토르를 그의 눈으로 보내 그들을 벌했습니다. 그녀는 세크메트가 되어 나일강이 빨갛게 흐를 때까지 인간들을 학살했습니다. 라는 자신의 명령을 후회하며 피처럼 빨갛게 물든 맥주로 그녀를 속였습니다. 그녀는 마시고 평화로운 하토르로 다시 돌아왔고, 인류는 구원받았습니다.",
    match_message_en="Your features carry the radiant joy of Hathor. There is beautiful warmth in your appearance—the look of one who brings pleasure and celebration to life, yet holds deeper power beneath the surface.",
    match_message_ko="당신의 이목구비는 하토르의 빛나는 기쁨을 담고 있습니다. 당신의 외모에는 아름다운 온기가 있습니다—삶에 즐거움과 축하를 가져다주지만, 표면 아래 더 깊은 힘을 가진 사람의 모습.",
    image_prompt="Beautiful Egyptian goddess with cow horns and sun disk headdress, sistrum in hand, surrounded by music and dancers, golden radiant beauty, expression of divine joy and hidden power, ancient Egyptian art style",
    visual_description="Beautiful radiant features, warm joyful eyes, golden luminous appearance, expression of pleasure-giving yet hinting at deeper power",
    aliases=["The Golden One", "Lady of the West"],
    era="Ancient Egypt",
    related_characters=["ra", "sekhmet", "horus", "isis"]
)

NUT_DESC = CharacterDescription(
    id="nut",
    name_en="Nut",
    name_ko="누트",
    tagline_en="Goddess of the Sky, Mother of Stars",
    tagline_ko="하늘의 여신, 별들의 어머니",
    description_en="""Nut is the goddess of the sky, depicted arching over the earth with her body forming the heavens. Each evening she swallows the sun, and each morning gives birth to it anew—the eternal cycle of night and day.

Her body is covered with stars, and she is mother to Osiris, Isis, Set, and Nephthys. Despite Ra's curse that she could bear children on no day of the year, Thoth won five extra days through gambling, allowing her to give birth.

Nut represents the protective canopy of the sky, the cosmic womb that contains all celestial bodies, and the eternal maternal cycle of death and rebirth.""",
    description_ko="""누트는 하늘의 여신으로, 그녀의 몸이 하늘을 형성하며 대지 위로 아치를 이루는 모습으로 묘사됩니다. 매일 저녁 그녀는 태양을 삼키고, 매일 아침 다시 낳습니다—밤과 낮의 영원한 순환.

그녀의 몸은 별들로 덮여 있고, 오시리스, 이시스, 세트, 네프티스의 어머니입니다. 라의 저주에도 불구하고—1년 중 어떤 날에도 아이를 낳을 수 없다는—토트가 도박을 통해 5일의 추가 날을 얻어 그녀가 아이를 낳을 수 있게 했습니다.

누트는 하늘의 보호하는 캐노피, 모든 천체를 담고 있는 우주적 자궁, 그리고 죽음과 재탄생의 영원한 모성적 순환을 대표합니다.""",
    traits_en=["Cosmic", "Maternal", "Protective", "Eternal", "Starry"],
    traits_ko=["우주적인", "모성적인", "보호하는", "영원한", "별이 빛나는"],
    story_en="Ra forbade Nut from giving birth on any day of the year. But Thoth played senet with the Moon and won enough light to create five new days outside the calendar. On these days, Nut gave birth to her five children, changing the course of Egyptian mythology forever.",
    story_ko="라는 누트가 1년 중 어떤 날에도 아이를 낳지 못하도록 금지했습니다. 하지만 토트가 달과 세네트를 하여 달력 밖의 5일을 만들 수 있는 충분한 빛을 얻었습니다. 이 날들에 누트는 다섯 자녀를 낳아 이집트 신화의 흐름을 영원히 바꾸었습니다.",
    match_message_en="Your features carry the cosmic embrace of Nut. There is encompassing grace in your appearance—the look of one who shelters all beneath them and embodies the eternal cycles of existence.",
    match_message_ko="당신의 이목구비는 누트의 우주적 포옹을 담고 있습니다. 당신의 외모에는 포괄하는 우아함이 있습니다—그 아래 모든 것을 감싸고 존재의 영원한 순환을 구현하는 사람의 모습.",
    image_prompt="Egyptian sky goddess arching over the earth, body covered with stars, swallowing and birthing the sun, cosmic blue and gold, expression of eternal maternal embrace, ancient Egyptian celestial art style",
    visual_description="Graceful elongated features, deep starry eyes, serene cosmic expression, appearance of one who encompasses all existence",
    aliases=["Lady of the Sky", "She Who Holds a Thousand Souls"],
    era="Ancient Egypt",
    related_characters=["geb", "ra", "osiris", "isis", "set", "nephthys"]
)

GEB_DESC = CharacterDescription(
    id="geb",
    name_en="Geb",
    name_ko="게브",
    tagline_en="God of the Earth, Father of Snakes",
    tagline_ko="대지의 신, 뱀들의 아버지",
    description_en="""Geb is the god of the earth, depicted lying beneath the arching sky goddess Nut, his sister-wife from whom he was separated by their father Shu. His laughter causes earthquakes, and his body forms the hills and valleys of the land.

As father of Osiris, Isis, Set, and Nephthys, Geb plays a crucial role in Egyptian mythology's central drama. He is also associated with snakes, which emerge from his earthly body, and with the growth of vegetation.

Geb represents the fertile earth that supports all life, the primordial foundation upon which existence rests, and the divine masculine principle that complements the sky.""",
    description_ko="""게브는 대지의 신으로, 아치형의 하늘 여신 누트 아래 누워 있는 모습으로 묘사됩니다. 누트는 그의 자매이자 아내로, 아버지 슈에 의해 그들은 분리되었습니다. 그의 웃음은 지진을 일으키고, 그의 몸은 땅의 언덕과 계곡을 형성합니다.

오시리스, 이시스, 세트, 네프티스의 아버지로서, 게브는 이집트 신화의 중심 드라마에서 중요한 역할을 합니다. 그는 또한 그의 대지의 몸에서 나오는 뱀들과, 식물의 성장과 연관됩니다.

게브는 모든 생명을 지탱하는 비옥한 대지, 존재가 쉬는 원초적 기초, 그리고 하늘을 보완하는 신성한 남성적 원리를 대표합니다.""",
    traits_en=["Earthly", "Foundational", "Fertile", "Fatherly", "Rumbling"],
    traits_ko=["대지의", "기초적인", "비옥한", "아버지같은", "우르릉거리는"],
    story_en="Geb and Nut loved each other so deeply they remained locked in embrace. Ra ordered Shu to separate them—Shu lifted Nut to become the sky while Geb remained below as earth. Geb's longing for Nut creates the mountains as he reaches up toward her.",
    story_ko="게브와 누트는 서로를 너무 깊이 사랑하여 포옹한 채로 남아 있었습니다. 라는 슈에게 그들을 분리하라고 명령했습니다—슈가 누트를 들어 올려 하늘이 되게 하고 게브는 아래에 대지로 남았습니다. 누트를 향한 게브의 그리움이 그녀를 향해 손을 뻗을 때 산을 만듭니다.",
    match_message_en="Your features carry the grounded strength of Geb. There is foundational stability in your appearance—the look of one who supports others and remains steadfast as the earth itself.",
    match_message_ko="당신의 이목구비는 게브의 근거 있는 힘을 담고 있습니다. 당신의 외모에는 기초적인 안정감이 있습니다—다른 이들을 지지하고 대지 자체처럼 꿋꿋이 남아 있는 사람의 모습.",
    image_prompt="Egyptian earth god reclining beneath sky, green-skinned with vegetation growing from body, reaching up toward stars, expression of longing and stability, ancient Egyptian earth tones",
    visual_description="Strong earthy features, deep grounded eyes, solid stable presence, expression of patient foundational strength",
    aliases=["Father of Snakes", "The Great Cackler"],
    era="Ancient Egypt",
    related_characters=["nut", "shu", "osiris", "isis", "set", "nephthys"]
)

PTAH_DESC = CharacterDescription(
    id="ptah",
    name_en="Ptah",
    name_ko="프타",
    tagline_en="Creator God of Craftsmen and Architects",
    tagline_ko="장인과 건축가의 창조신",
    description_en="""Ptah is the creator god of Memphis, who brought the world into existence through the power of thought and speech. Unlike other creation myths involving physical acts, Ptah conceived the world in his heart and spoke it into being.

As patron of craftsmen, sculptors, and architects, Ptah represents divine creativity made manifest in human hands. Every act of creation—from building pyramids to carving statues—is an echo of his original creative word.

Ptah represents the creative power of the mind, the sacred nature of craftsmanship, and the idea that thought precedes and shapes reality.""",
    description_ko="""프타는 멤피스의 창조신으로, 생각과 말의 힘으로 세계를 존재하게 했습니다. 물리적 행위를 포함하는 다른 창조 신화와 달리, 프타는 세계를 마음에서 구상하고 말로 존재하게 했습니다.

장인, 조각가, 건축가의 수호자로서, 프타는 인간의 손에서 나타난 신성한 창의성을 대표합니다. 피라미드 건설에서 조각상 조각까지 모든 창조 행위는 그의 원래 창조적 말의 메아리입니다.

프타는 정신의 창조적 힘, 장인 정신의 신성한 본성, 그리고 생각이 현실에 선행하고 형성한다는 아이디어를 대표합니다.""",
    traits_en=["Creative", "Thoughtful", "Skilled", "Speaking", "Manifesting"],
    traits_ko=["창조적인", "사려 깊은", "숙련된", "말하는", "나타나게 하는"],
    story_en="In the beginning, Ptah conceived all things in his heart—the gods, the earth, the creatures. Then he spoke their names, and they came into being. Every word Ptah uttered became reality, and creation continues wherever craftsmen shape matter with skill and intention.",
    story_ko="태초에 프타는 모든 것을 마음에서 구상했습니다—신들, 대지, 피조물들. 그런 다음 그는 그들의 이름을 말했고, 그들이 존재하게 되었습니다. 프타가 말한 모든 단어가 현실이 되었고, 창조는 장인들이 기술과 의도로 물질을 형성하는 곳 어디서나 계속됩니다.",
    match_message_en="Your features carry the creative vision of Ptah. There is craftsman's wisdom in your appearance—the look of one who can conceive beauty and bring it into being through skilled intention.",
    match_message_ko="당신의 이목구비는 프타의 창조적 비전을 담고 있습니다. 당신의 외모에는 장인의 지혜가 있습니다—아름다움을 구상하고 숙련된 의도를 통해 그것을 존재하게 할 수 있는 사람의 모습.",
    image_prompt="Egyptian creator god in tight-fitting garment holding was-scepter, green or blue skin, craftsmen and builders working in background, creative light emanating from mouth, ancient Egyptian art style",
    visual_description="Thoughtful focused features, creative intelligent eyes, composed dignified bearing, expression of one who manifests thought into reality",
    aliases=["The Opener", "Lord of Truth"],
    era="Ancient Egypt",
    related_characters=["sekhmet", "thoth", "ra", "imhotep"]
)

KHNUM_DESC = CharacterDescription(
    id="khnum",
    name_en="Khnum",
    name_ko="크눔",
    tagline_en="Ram-Headed God of Creation and the Nile",
    tagline_ko="양 머리의 창조신과 나일의 신",
    description_en="""Khnum is the ram-headed god who creates human beings and their ka (soul) on his potter's wheel. He was believed to shape each child's body from clay before placing it in the mother's womb.

Associated with the Nile's source and its annual life-giving flood, Khnum was worshipped as the creator of all things that come from water and earth. His temples stood near the cataracts where the Nile was believed to originate.

Khnum represents the divine craftsman who shapes individual lives, the creative power of the Nile, and the unique formation of each soul.""",
    description_ko="""크눔은 물레에서 인간과 그들의 카(영혼)를 창조하는 양 머리 신입니다. 그는 각 아이의 몸을 점토로 빚어 어머니의 자궁에 넣기 전에 형성한다고 믿어졌습니다.

나일강의 원천과 연간 생명을 주는 홍수와 연관된 크눔은 물과 땅에서 오는 모든 것의 창조자로 숭배되었습니다. 그의 신전은 나일강이 시작된다고 믿어지는 폭포 근처에 서 있었습니다.

크눔은 개인의 삶을 형성하는 신성한 장인, 나일강의 창조적 힘, 그리고 각 영혼의 고유한 형성을 대표합니다.""",
    traits_en=["Creative", "Forming", "Fertile", "Individuating", "Watery"],
    traits_ko=["창조적인", "형성하는", "비옥한", "개성화하는", "물의"],
    story_en="Before each child is born, Khnum shapes their body on his divine potter's wheel, crafting each person uniquely. He then forms their ka, their spiritual double, ensuring that no two souls are alike. The flood of the Nile is his creative power flowing forth.",
    story_ko="각 아이가 태어나기 전, 크눔은 그의 신성한 물레에서 그들의 몸을 빚어, 각 사람을 독특하게 만듭니다. 그런 다음 그는 그들의 영적 분신인 카를 형성하여, 두 영혼이 같지 않도록 합니다. 나일강의 홍수는 그의 창조적 힘이 흘러나오는 것입니다.",
    match_message_en="Your features carry the individual craftsmanship of Khnum. There is unique shaping in your appearance—the look of one carefully formed with purpose, unlike any other.",
    match_message_ko="당신의 이목구비는 크눔의 개별적인 장인 정신을 담고 있습니다. 당신의 외모에는 독특한 형성이 있습니다—다른 어떤 것과도 다르게 목적을 가지고 세심하게 형성된 사람의 모습.",
    image_prompt="Egyptian ram-headed god at potter's wheel, shaping human figure from clay, Nile River flowing behind, divine creative light, expression of focused craftsmanship, ancient Egyptian art style",
    visual_description="Wise craftsman features, focused creative eyes, patient deliberate expression, appearance of one who shapes each being with care",
    aliases=["The Potter", "Lord of Created Things"],
    era="Ancient Egypt",
    related_characters=["ptah", "ra", "heqet", "satis"]
)

ATUM_DESC = CharacterDescription(
    id="atum",
    name_en="Atum",
    name_ko="아툼",
    tagline_en="The Complete One, First of the Gods",
    tagline_ko="완전한 자, 신들 중 첫 번째",
    description_en="""Atum is the primordial creator god of Heliopolis, the 'Complete One' who existed before creation and will exist after all things end. He emerged from the primordial waters of Nun and created the first gods—Shu and Tefnut—from himself.

As the setting sun, Atum represents completion, the end of the day's cycle, and the return to the source. He is both the beginning and the end, containing within himself all potential for creation.

Atum represents primordial completeness, the self-generating power of creation, and the cycle that returns all things to their origin.""",
    description_ko="""아툼은 헬리오폴리스의 원초적 창조신으로, 창조 이전에 존재했고 모든 것이 끝난 후에도 존재할 '완전한 자'입니다. 그는 눈의 태초의 물에서 나와 첫 번째 신들—슈와 테프누트—를 자신에게서 창조했습니다.

지는 태양으로서 아툼은 완성, 하루 주기의 끝, 그리고 근원으로의 복귀를 대표합니다. 그는 시작이자 끝이며, 창조의 모든 잠재력을 자신 안에 담고 있습니다.

아툼은 원초적 완전함, 창조의 자기 생성 힘, 그리고 모든 것을 그 기원으로 되돌리는 순환을 대표합니다.""",
    traits_en=["Complete", "Primordial", "Setting", "Self-creating", "Finishing"],
    traits_ko=["완전한", "원초적인", "지는", "자기 창조하는", "완결하는"],
    story_en="Before anything existed, Atum stood alone on the first mound to emerge from chaos. He created Shu (air) and Tefnut (moisture) from himself, and from them came all other gods and creation. At the end of time, all will return to Atum's primordial unity.",
    story_ko="아무것도 존재하기 전, 아툼은 혼돈에서 나온 첫 번째 언덕 위에 홀로 서 있었습니다. 그는 자신에게서 슈(공기)와 테프누트(습기)를 창조했고, 그들로부터 다른 모든 신들과 창조물이 왔습니다. 시간의 끝에, 모든 것은 아툼의 원초적 통일로 돌아갈 것입니다.",
    match_message_en="Your features carry the primordial completeness of Atum. There is self-contained wholeness in your appearance—the look of one who contains within themselves everything needed for creation.",
    match_message_ko="당신의 이목구비는 아툼의 원초적 완전함을 담고 있습니다. 당신의 외모에는 자기 충족적인 전체성이 있습니다—창조에 필요한 모든 것을 자신 안에 담고 있는 사람의 모습.",
    image_prompt="Ancient Egyptian creator god emerging from primordial waters, wearing double crown, setting sun behind, standing on first mound of creation, expression of serene completion, ancient Egyptian art style",
    visual_description="Serene complete features, ancient knowing eyes, self-contained presence, expression of one who is both beginning and end",
    aliases=["The Complete One", "Lord of Totality"],
    era="Ancient Egypt",
    related_characters=["ra", "shu", "tefnut", "nun"]
)

SEKHMET_EXTENDED_DESC = CharacterDescription(
    id="sekhmet",
    name_en="Sekhmet",
    name_ko="세크메트",
    tagline_en="Lioness Goddess of War and Healing",
    tagline_ko="전쟁과 치유의 암사자 여신",
    description_en="""Sekhmet is the fierce lioness-headed goddess of war, destruction, and paradoxically, healing. Her name means 'The Powerful One,' and her breath created the desert. She represents the scorching, destructive heat of the sun.

As the Eye of Ra sent to punish humanity, Sekhmet's bloodlust was so great she nearly destroyed all human life. Only by tricking her with beer dyed red like blood was she pacified and transformed back to gentle Hathor.

Sekhmet represents the terrible aspect of divine power, the fever that both kills and cleanses, and the truth that destruction and healing are two faces of the same force.""",
    description_ko="""세크메트는 전쟁, 파괴, 그리고 역설적으로 치유의 사나운 암사자 머리 여신입니다. 그녀의 이름은 '강력한 자'를 의미하며, 그녀의 숨결이 사막을 만들었습니다. 그녀는 태양의 타오르는 파괴적인 열기를 대표합니다.

인류를 벌하기 위해 보내진 라의 눈으로서, 세크메트의 피에 대한 갈증은 너무 커서 모든 인간 생명을 거의 파괴할 뻔했습니다. 피처럼 빨갛게 물든 맥주로 그녀를 속여서야 그녀는 진정되고 부드러운 하토르로 다시 변했습니다.

세크메트는 신성한 힘의 끔찍한 면, 죽이고 정화하는 열병, 그리고 파괴와 치유가 같은 힘의 두 얼굴이라는 진실을 대표합니다.""",
    traits_en=["Fierce", "Destructive", "Healing", "Powerful", "Passionate"],
    traits_ko=["사나운", "파괴적인", "치유하는", "강력한", "열정적인"],
    story_en="Ra sent Sekhmet to destroy rebellious humanity. She waded through blood, unable to stop killing. To save the survivors, Ra flooded the fields with 7,000 jars of beer dyed red. Sekhmet drank, thinking it was blood, and awoke peaceful—her destructive rage ended.",
    story_ko="라는 반역하는 인류를 멸망시키기 위해 세크메트를 보냈습니다. 그녀는 피 속을 걸으며 죽이는 것을 멈출 수 없었습니다. 생존자들을 구하기 위해, 라는 7,000병의 빨갛게 물든 맥주로 들판을 채웠습니다. 세크메트는 그것이 피라고 생각하고 마셨고, 평화롭게 깨어났습니다—그녀의 파괴적인 분노가 끝났습니다.",
    match_message_en="Your features carry the fierce power of Sekhmet. There is warrior strength in your appearance—the look of one who can destroy or heal with equal intensity, channeling powerful forces for protection.",
    match_message_ko="당신의 이목구비는 세크메트의 사나운 힘을 담고 있습니다. 당신의 외모에는 전사의 힘이 있습니다—동등한 강도로 파괴하거나 치유할 수 있고, 보호를 위해 강력한 힘을 전달하는 사람의 모습.",
    image_prompt="Fierce Egyptian lioness-headed goddess in red dress, breathing fire, solar disk crown, battlefield or healing temple behind, expression of terrible divine power, ancient Egyptian art style",
    visual_description="Fierce powerful features, blazing intense eyes, commanding fearsome presence, expression of one who destroys to protect",
    aliases=["The Powerful One", "Eye of Ra"],
    era="Ancient Egypt",
    related_characters=["ra", "hathor", "ptah", "bastet"]
)

ANUKET_DESC = CharacterDescription(
    id="anuket",
    name_en="Anuket",
    name_ko="아누켓",
    tagline_en="Goddess of the Nile and Nourishment",
    tagline_ko="나일강과 양분의 여신",
    description_en="""Anuket is the goddess of the Nile River, particularly the cataracts and the annual inundation that brought fertile soil to Egypt. She personifies the rushing waters that nourished civilization, wearing a headdress of feathers representing the river's flow.

Worshipped especially in Nubia and at Elephantine, Anuket was called upon to ensure good floods—neither too little nor too destructive. She embodied the life-giving generosity of the river upon which all Egypt depended.

Anuket represents the nourishing flow of life, the abundance that comes from natural cycles, and the gratitude owed to forces that sustain us.""",
    description_ko="""아누켓은 나일강의 여신으로, 특히 폭포와 이집트에 비옥한 토양을 가져오는 연간 범람을 관장합니다. 그녀는 문명을 양분하는 급류를 의인화하며, 강의 흐름을 나타내는 깃털 머리장식을 착용합니다.

특히 누비아와 엘레판틴에서 숭배받았던 아누켓은 좋은 홍수—너무 적지도 파괴적이지도 않은—를 보장해달라고 불렸습니다. 그녀는 모든 이집트가 의존하는 강의 생명을 주는 관대함을 구현했습니다.

아누켓은 생명의 양분하는 흐름, 자연 순환에서 오는 풍요, 그리고 우리를 지탱하는 힘에 대한 감사를 대표합니다.""",
    traits_en=["Nourishing", "Flowing", "Abundant", "Rushing", "Generous"],
    traits_ko=["양분하는", "흐르는", "풍요로운", "급류하는", "관대한"],
    story_en="Each year when the Nile began to rise, Egyptians celebrated the Festival of Anuket, casting offerings into the river and thanking her for the flood's gifts. Her waters carried the black soil that made Egypt the breadbasket of the ancient world.",
    story_ko="매년 나일강이 상승하기 시작할 때, 이집트인들은 아누켓 축제를 축하하며 강에 제물을 던지고 홍수의 선물에 감사했습니다. 그녀의 물은 이집트를 고대 세계의 곡창 지대로 만든 검은 토양을 실어 날랐습니다.",
    match_message_en="Your features carry the nourishing grace of Anuket. There is generous flow in your appearance—the look of one who brings abundance and sustains others with life-giving generosity.",
    match_message_ko="당신의 이목구비는 아누켓의 양분하는 우아함을 담고 있습니다. 당신의 외모에는 관대한 흐름이 있습니다—풍요를 가져오고 생명을 주는 관대함으로 다른 이들을 지탱하는 사람의 모습.",
    image_prompt="Egyptian river goddess with tall feather headdress, holding papyrus and ankh, standing in rushing Nile waters, fertile black soil on banks, expression of generous abundance, ancient Egyptian art style",
    visual_description="Graceful flowing features, generous warm eyes, fluid elegant presence, expression of life-giving abundance",
    aliases=["Embracer of the Nile", "Lady of the Cataracts"],
    era="Ancient Egypt",
    related_characters=["khnum", "satis", "hapi"]
)


# Dictionary of additional Egyptian descriptions
EGYPTIAN_ADDITIONAL_DESCRIPTIONS = {
    "nephthys": NEPHTHYS_DESC,
    "maat": MA_AT_DESC,
    "sobek": SOBEK_DESC,
    "hathor": HATHOR_DESC,
    "nut": NUT_DESC,
    "geb": GEB_DESC,
    "ptah": PTAH_DESC,
    "khnum": KHNUM_DESC,
    "atum": ATUM_DESC,
    "sekhmet": SEKHMET_EXTENDED_DESC,
    "anuket": ANUKET_DESC,
}

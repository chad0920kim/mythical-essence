"""
Greek Mythology - Additional Character Descriptions
Extends the base descriptions.py with more Greek figures
"""
from .descriptions import CharacterDescription


# Additional Greek Mythology Figures (to reach 20+)

DEMETER_DESC = CharacterDescription(
    id="demeter",
    name_en="Demeter",
    name_ko="데메테르",
    tagline_en="Goddess of Harvest, Agriculture, and Seasons",
    tagline_ko="수확, 농업, 계절의 여신",
    description_en="""Demeter is the goddess of the harvest, agriculture, fertility, and the sacred law. She presides over the cycle of life and death, grains and the fertility of the earth. As one of the original six Olympians, she holds immense power over the natural world.

Her grief when Hades abducted her daughter Persephone caused all plants to wither and die, bringing the first winter to the world. Only when Persephone returns does spring come again.

Demeter represents the nurturing mother who provides sustenance to all living things, but also the terrible power of nature when her gifts are withdrawn.""",
    description_ko="""데메테르는 수확, 농업, 다산, 신성한 법의 여신입니다. 그녀는 생사의 순환, 곡물과 대지의 비옥함을 주관합니다. 원래 여섯 올림포스 신 중 하나로서, 그녀는 자연 세계에 대한 막대한 힘을 가지고 있습니다.

하데스가 딸 페르세포네를 납치했을 때 그녀의 슬픔은 모든 식물을 시들고 죽게 하여 세상에 첫 번째 겨울을 가져왔습니다. 페르세포네가 돌아올 때만 봄이 다시 옵니다.

데메테르는 모든 생명체에게 양식을 제공하는 양육하는 어머니를 대표하지만, 그녀의 선물이 철회될 때 자연의 끔찍한 힘도 대표합니다.""",
    traits_en=["Nurturing", "Grieving", "Powerful", "Seasonal", "Maternal"],
    traits_ko=["양육하는", "슬퍼하는", "강력한", "계절적인", "모성적인"],
    story_en="When Persephone was taken, Demeter wandered the earth in grief, letting no crops grow. Famine spread until Zeus intervened, but because Persephone had eaten pomegranate seeds in the underworld, she must return there each year—and so winter returns.",
    story_ko="페르세포네가 잡혀갔을 때, 데메테르는 슬픔 속에 대지를 헤매며 어떤 작물도 자라지 못하게 했습니다. 제우스가 개입할 때까지 기근이 퍼졌지만, 페르세포네가 지하세계에서 석류 씨앗을 먹었기 때문에 매년 그곳으로 돌아가야 합니다—그래서 겨울이 돌아옵니다.",
    match_message_en="Your features reflect the nurturing power of Demeter. There is a life-giving warmth to your appearance, but also a depth of feeling that speaks of one who loves fiercely and grieves deeply.",
    match_message_ko="당신의 이목구비는 데메테르의 양육하는 힘을 반영합니다. 당신의 외모에는 생명을 주는 온기가 있지만, 맹렬하게 사랑하고 깊이 슬퍼하는 사람을 말해주는 감정의 깊이도 있습니다.",
    image_prompt="Majestic Greek goddess with wheat crown and golden harvest robes, holding sheaves of grain and torch, surrounded by crops and flowers, both nurturing and sorrowful expression, autumn colors",
    visual_description="Mature maternal features, warm but sad eyes, strong nurturing presence, expression of both abundance and loss",
    aliases=["Ceres", "Mother of Grain"],
    era="Ancient Greece",
    related_characters=["persephone", "zeus", "hades", "triptolemus"]
)

HEPHAESTUS_DESC = CharacterDescription(
    id="hephaestus",
    name_en="Hephaestus",
    name_ko="헤파이스토스",
    tagline_en="God of Fire, Forge, and Craftsmanship",
    tagline_ko="불, 대장간, 장인정신의 신",
    description_en="""Hephaestus is the god of fire, metalworking, stone masonry, forges, and the art of sculpture. He is the craftsman of the gods, creating their weapons, armor, and the most wondrous artifacts in existence.

Born lame—or made so when Hera threw him from Olympus in disgust—Hephaestus turned his perceived weakness into unmatched skill. His forge beneath Mount Etna produces works of such beauty and power that even other gods marvel.

Though married to Aphrodite, their union was unhappy. Yet Hephaestus represents the dignity of honest labor, the beauty that emerges from patient craft, and the truth that worth is measured by what one creates, not how one appears.""",
    description_ko="""헤파이스토스는 불, 금속 세공, 석조, 대장간, 조각 예술의 신입니다. 그는 신들의 장인으로, 그들의 무기, 갑옷, 존재하는 가장 놀라운 공예품들을 만듭니다.

절름발이로 태어났거나—헤라가 혐오감에 올림포스에서 그를 던졌을 때 그렇게 되었거나—헤파이스토스는 자신의 인식된 약점을 비할 데 없는 기술로 바꾸었습니다. 에트나 산 아래 그의 대장간은 다른 신들조차 경탄하는 아름다움과 힘의 작품들을 생산합니다.

아프로디테와 결혼했지만, 그들의 결합은 불행했습니다. 그러나 헤파이스토스는 정직한 노동의 존엄성, 인내하는 장인정신에서 나오는 아름다움, 그리고 가치는 외모가 아닌 창조하는 것으로 측정된다는 진실을 대표합니다.""",
    traits_en=["Skilled", "Patient", "Creative", "Resilient", "Underestimated"],
    traits_ko=["숙련된", "인내하는", "창조적인", "탄력적인", "과소평가된"],
    story_en="Hephaestus crafted Achilles' legendary armor, Hermes' winged sandals, and the chains that bound Prometheus. When he caught Aphrodite with Ares, he trapped them in an unbreakable golden net for all Olympus to see.",
    story_ko="헤파이스토스는 아킬레스의 전설적인 갑옷, 헤르메스의 날개 달린 샌들, 프로메테우스를 묶은 사슬을 만들었습니다. 아프로디테가 아레스와 함께 있는 것을 발견했을 때, 그는 모든 올림포스가 볼 수 있도록 깨지지 않는 황금 그물에 그들을 가두었습니다.",
    match_message_en="Your features carry the patient determination of Hephaestus. There is a quiet strength to your appearance—the look of one who creates beauty through dedicated work rather than natural gifts.",
    match_message_ko="당신의 이목구비는 헤파이스토스의 인내하는 결단력을 담고 있습니다. 당신의 외모에는 조용한 힘이 있습니다—자연적 재능보다 헌신적인 작업을 통해 아름다움을 창조하는 사람의 모습.",
    image_prompt="Muscular Greek god at the forge, working with hammer and tongs, fire illuminating his face, surrounded by wondrous creations, one leg shorter but standing proud, focused craftsman expression",
    visual_description="Strong weathered features, focused intense eyes, powerful hands, expression of deep concentration and creative pride",
    aliases=["Vulcan", "The Crippled God", "The Smith"],
    era="Ancient Greece",
    related_characters=["aphrodite", "ares", "hera", "zeus", "athena"]
)

EROS_DESC = CharacterDescription(
    id="eros",
    name_en="Eros",
    name_ko="에로스",
    tagline_en="God of Love and Desire",
    tagline_ko="사랑과 욕망의 신",
    description_en="""Eros is the god of love, desire, and attraction, whose golden arrows can make any being fall helplessly in love. In some myths, he is a primordial god as old as creation itself; in others, he is the mischievous son of Aphrodite.

His power is perhaps the most dangerous of all the gods—no one, not even mighty Zeus, is immune to his arrows. Love, once struck, cannot be reasoned with or resisted. Eros understands that love is both humanity's greatest blessing and its most unpredictable force.

Though often depicted as a playful youth, Eros is far from innocent. His arrows have caused wars, broken kingdoms, and driven gods and mortals to madness and despair—and to the heights of joy.""",
    description_ko="""에로스는 사랑, 욕망, 매력의 신으로, 그의 황금 화살은 어떤 존재든 무기력하게 사랑에 빠지게 만들 수 있습니다. 일부 신화에서 그는 창조 자체만큼 오래된 원초적 신이고; 다른 신화에서는 아프로디테의 장난꾸러기 아들입니다.

그의 힘은 아마도 모든 신들 중 가장 위험합니다—강력한 제우스조차도 그의 화살에 면역이 아닙니다. 사랑은 한번 맞으면 이성이나 저항이 통하지 않습니다. 에로스는 사랑이 인류의 가장 큰 축복이자 가장 예측 불가능한 힘이라는 것을 이해합니다.

종종 장난스러운 청년으로 묘사되지만, 에로스는 결코 순진하지 않습니다. 그의 화살은 전쟁을 일으키고, 왕국을 무너뜨리고, 신과 인간을 광기와 절망으로—그리고 기쁨의 정점으로 몰아넣었습니다.""",
    traits_en=["Playful", "Powerful", "Unpredictable", "Mischievous", "Irresistible"],
    traits_ko=["장난스러운", "강력한", "예측불가한", "장난꾸러기의", "저항할 수 없는"],
    story_en="Eros fell in love with the mortal Psyche but could only visit her in darkness. When she disobeyed and saw his face by lamplight, he fled. Only after Psyche completed impossible tasks set by Aphrodite was she reunited with Eros and made immortal.",
    story_ko="에로스는 인간 프시케와 사랑에 빠졌지만 어둠 속에서만 그녀를 방문할 수 있었습니다. 그녀가 불순종하고 램프 빛으로 그의 얼굴을 보았을 때, 그는 도망쳤습니다. 프시케가 아프로디테가 정한 불가능한 과제를 완수한 후에야 에로스와 재회하고 불멸이 되었습니다.",
    match_message_en="Your features carry the captivating charm of Eros. There is an irresistible quality to your appearance—the look of one who understands the power of attraction and connection.",
    match_message_ko="당신의 이목구비는 에로스의 매혹적인 매력을 담고 있습니다. 당신의 외모에는 저항할 수 없는 품질이 있습니다—매력과 연결의 힘을 이해하는 사람의 모습.",
    image_prompt="Beautiful winged youth with golden bow and arrows, playful yet knowing expression, surrounded by hearts and flowers, ethereal romantic lighting, mischievous divine presence",
    visual_description="Youthful beautiful features, playful knowing eyes, charming smile, appearance of eternal youth and irresistible attraction",
    aliases=["Cupid", "Amor"],
    era="Ancient Greece",
    related_characters=["aphrodite", "psyche", "ares", "pan"]
)

PAN_DESC = CharacterDescription(
    id="pan",
    name_en="Pan",
    name_ko="판",
    tagline_en="God of the Wild, Shepherds, and Rustic Music",
    tagline_ko="야생, 목자, 전원 음악의 신",
    description_en="""Pan is the god of the wild, shepherds, flocks, nature, mountain wilds, and rustic music. With his goat legs, horns, and shaggy hair, he represents untamed nature and the primal forces that civilization tries to suppress.

He roams the forests and mountains playing his pan pipes, whose haunting music can inspire both joy and the sudden terror called "panic." His domain is the wild spaces between settlements, where nature rules and human order does not reach.

Pan is associated with sexuality and fertility, often pursuing nymphs through the woods. Yet he also represents the simple joy of pastoral life, the bond between shepherd and flock, and the importance of wilderness in a civilized world.""",
    description_ko="""판은 야생, 목자, 양떼, 자연, 산악 야생, 전원 음악의 신입니다. 염소 다리, 뿔, 덥수룩한 머리카락으로 그는 길들여지지 않은 자연과 문명이 억압하려는 원초적 힘을 대표합니다.

그는 숲과 산을 돌아다니며 팬 파이프를 연주하는데, 그 매혹적인 음악은 기쁨과 "패닉"이라 불리는 갑작스러운 공포 모두를 불러일으킬 수 있습니다. 그의 영역은 정착지 사이의 야생 공간으로, 자연이 지배하고 인간의 질서가 닿지 않는 곳입니다.

판은 성욕과 다산과 연관되어, 종종 숲을 통해 님프들을 쫓습니다. 그러나 그는 또한 전원 생활의 단순한 기쁨, 목자와 양떼 사이의 유대, 문명화된 세계에서 야생의 중요성을 대표합니다.""",
    traits_en=["Wild", "Musical", "Lusty", "Frightening", "Natural"],
    traits_ko=["야생의", "음악적인", "정욕적인", "무서운", "자연적인"],
    story_en="Pan pursued the nymph Syrinx, who fled from him and begged the river to save her. She was transformed into water reeds. Pan, finding only reeds where his love had stood, fashioned the first pan pipes from them, forever playing songs of his lost love.",
    story_ko="판은 님프 시링크스를 쫓았는데, 그녀는 그에게서 도망쳐 강에게 구해달라고 간청했습니다. 그녀는 갈대로 변했습니다. 판은 사랑이 서 있던 곳에서 오직 갈대만 발견하고, 그것으로 최초의 팬 파이프를 만들어 영원히 잃어버린 사랑의 노래를 연주합니다.",
    match_message_en="Your features carry the wild energy of Pan. There is an untamed, natural quality to your appearance—the look of one connected to primal forces and the joy of uninhibited expression.",
    match_message_ko="당신의 이목구비는 판의 야생적 에너지를 담고 있습니다. 당신의 외모에는 길들여지지 않은 자연적 품질이 있습니다—원초적 힘과 억제 없는 표현의 기쁨에 연결된 사람의 모습.",
    image_prompt="Wild god with goat legs and horns, playing pan pipes in forest glade, surrounded by forest animals and dancing, mischievous wild expression, dappled forest sunlight, Greek pastoral setting",
    visual_description="Wild unkempt features, bright mischievous eyes, wide grin, appearance of untamed nature and primal energy",
    aliases=["Faunus"],
    era="Ancient Greece",
    related_characters=["hermes", "dionysus", "syrinx", "nymphs"]
)

PROMETHEUS_DESC = CharacterDescription(
    id="prometheus",
    name_en="Prometheus",
    name_ko="프로메테우스",
    tagline_en="Titan of Forethought, Bringer of Fire",
    tagline_ko="선견의 티탄, 불의 전달자",
    description_en="""Prometheus is the Titan who shaped humanity from clay and then defied the gods to give them fire. His gift was not merely flames, but civilization itself—knowledge, technology, and the spark of progress that would let humans rise above mere animals.

Zeus punished Prometheus terribly for this gift: chained to a mountain, an eagle ate his liver each day, which regenerated each night for eternal torment. Yet Prometheus never regretted his choice, enduring millennia of suffering for the sake of humanity.

He represents the divine spark of rebellion against tyranny, the willingness to suffer for others' benefit, and the belief that knowledge should never be hoarded by the powerful.""",
    description_ko="""프로메테우스는 점토로 인류를 빚고 그 후 신들을 거역하여 그들에게 불을 준 티탄입니다. 그의 선물은 단순한 불꽃이 아니라 문명 그 자체—지식, 기술, 그리고 인간이 단순한 동물 위로 오를 수 있게 하는 진보의 불꽃이었습니다.

제우스는 이 선물에 대해 프로메테우스를 끔찍하게 벌했습니다: 산에 묶여, 독수리가 매일 그의 간을 먹었고, 영원한 고문을 위해 매일 밤 재생되었습니다. 그러나 프로메테우스는 인류를 위해 수천 년의 고통을 견디며 결코 자신의 선택을 후회하지 않았습니다.

그는 폭정에 대한 반항의 신성한 불꽃, 다른 사람들의 이익을 위해 고통받으려는 의지, 그리고 지식은 결코 권력자들에 의해 독점되어서는 안 된다는 믿음을 대표합니다.""",
    traits_en=["Defiant", "Sacrificial", "Wise", "Suffering", "Benevolent"],
    traits_ko=["반항적인", "희생적인", "지혜로운", "고통받는", "자비로운"],
    story_en="Prometheus stole fire from Olympus hidden in a fennel stalk and gave it to humanity. For this crime, Zeus had him chained to a rock where an eagle tore at his liver daily. Only after thousands of years did Heracles finally free him.",
    story_ko="프로메테우스는 회향 줄기에 숨겨 올림포스에서 불을 훔쳐 인류에게 주었습니다. 이 죄로 제우스는 그를 바위에 묶어 독수리가 매일 그의 간을 찢게 했습니다. 수천 년 후에야 헤라클레스가 마침내 그를 해방시켰습니다.",
    match_message_en="Your features carry the noble defiance of Prometheus. There is a suffering strength to your appearance—the look of one who would endure any pain to help others rise.",
    match_message_ko="당신의 이목구비는 프로메테우스의 고귀한 반항을 담고 있습니다. 당신의 외모에는 고통받는 힘이 있습니다—다른 사람들이 일어서도록 돕기 위해 어떤 고통도 견딜 사람의 모습.",
    image_prompt="Noble Titan chained to mountain rock, eagle nearby, fire glowing in background, dignified suffering expression, dramatic stormy sky, ancient Greek tragic hero aesthetic",
    visual_description="Noble weathered features, eyes that have seen eternity of suffering yet remain unbroken, dignified tragic expression",
    aliases=["The Fire-Bringer", "The Fore-Thinker"],
    era="Ancient Greece",
    related_characters=["zeus", "heracles", "epimetheus", "pandora", "hephaestus"]
)

HERCULES_DESC = CharacterDescription(
    id="hercules",
    name_en="Heracles",
    name_ko="헤라클레스",
    tagline_en="Greatest of Heroes, Champion of Mankind",
    tagline_ko="가장 위대한 영웅, 인류의 챔피언",
    description_en="""Heracles is the greatest of all Greek heroes, son of Zeus and the mortal Alcmene. His incredible strength and courage made him the champion of humanity against monsters and impossible challenges, and he eventually earned immortality among the gods.

Driven mad by Hera, he killed his own family—a tragedy that led to his famous Twelve Labors as penance. Each task seemed impossible: slaying the Nemean Lion, capturing Cerberus, cleaning the Augean Stables. Yet Heracles completed them all through strength, courage, and cleverness.

Beyond his strength, Heracles represents the ability to overcome one's darkest moments through heroic action. He is proof that even after terrible falls, redemption is possible through determined effort and courage.""",
    description_ko="""헤라클레스는 모든 그리스 영웅 중 가장 위대한 존재로, 제우스와 인간 알크메네의 아들입니다. 그의 믿을 수 없는 힘과 용기는 그를 괴물과 불가능한 도전에 맞서는 인류의 챔피언으로 만들었고, 결국 신들 사이에서 불멸을 얻었습니다.

헤라에 의해 미치광이가 되어 자신의 가족을 죽였고—이 비극이 속죄로서 그의 유명한 열두 과업으로 이어졌습니다. 각 과제는 불가능해 보였습니다: 네메아의 사자 죽이기, 케르베로스 포획하기, 아우게이아스의 마구간 청소하기. 그러나 헤라클레스는 힘, 용기, 영리함을 통해 모두 완수했습니다.

힘 외에도, 헤라클레스는 영웅적 행동을 통해 가장 어두운 순간을 극복하는 능력을 대표합니다. 그는 끔찍한 추락 후에도 결단력 있는 노력과 용기를 통해 구원이 가능하다는 증거입니다.""",
    traits_en=["Strong", "Courageous", "Redeemed", "Enduring", "Heroic"],
    traits_ko=["강한", "용감한", "구원받은", "견디는", "영웅적인"],
    story_en="Heracles descended to the underworld and captured Cerberus bare-handed—the only mortal ever to enter Hades' realm and return. Upon completing his Twelve Labors, he was granted immortality and a place among the Olympian gods.",
    story_ko="헤라클레스는 지하세계로 내려가 맨손으로 케르베로스를 포획했습니다—하데스의 영역에 들어가 돌아온 유일한 필멸자. 열두 과업을 완수한 후, 그는 불멸과 올림포스 신들 사이의 자리를 부여받았습니다.",
    match_message_en="Your features carry the mighty determination of Heracles. There is an immense strength to your appearance—the look of one who can overcome any obstacle through sheer will and courage.",
    match_message_ko="당신의 이목구비는 헤라클레스의 강력한 결단력을 담고 있습니다. 당신의 외모에는 엄청난 힘이 있습니다—순수한 의지와 용기로 어떤 장애물도 극복할 수 있는 사람의 모습.",
    image_prompt="Mighty Greek hero with lion skin cloak and club, incredibly muscular, determined expression, battling monsters or standing victorious, Greek temple background, heroic divine light",
    visual_description="Powerfully muscular features, determined intense eyes, strong jaw, expression of unstoppable determination and strength",
    aliases=["Hercules", "Alcides"],
    era="Ancient Greece",
    related_characters=["zeus", "hera", "athena", "hades", "cerberus"]
)

HELIOS_DESC = CharacterDescription(
    id="helios",
    name_en="Helios",
    name_ko="헬리오스",
    tagline_en="Titan God of the Sun",
    tagline_ko="태양의 티탄 신",
    description_en="""Helios is the Titan god of the sun, who drives his golden chariot across the sky each day from east to west, bringing light to the world. From his position above, he sees and hears everything that happens under the sun.

Unlike Apollo who later became associated with the sun, Helios is the sun itself personified—the actual fiery orb that crosses the sky. Each morning he rises from the river Oceanus and each night returns, passing beneath the earth.

He is the all-seeing witness, often called upon in oaths because nothing escapes his notice. It was Helios who told Demeter what happened to Persephone, and who revealed Aphrodite's affair with Ares.""",
    description_ko="""헬리오스는 태양의 티탄 신으로, 매일 황금 전차를 타고 동쪽에서 서쪽으로 하늘을 가로질러 세상에 빛을 가져다줍니다. 위에서 바라보는 그의 위치에서 그는 태양 아래 일어나는 모든 것을 보고 듣습니다.

나중에 태양과 연관된 아폴론과 달리, 헬리오스는 태양 자체의 의인화입니다—하늘을 가로지르는 실제 불타는 구체. 매일 아침 그는 오케아노스 강에서 떠오르고 매일 밤 돌아가며, 땅 아래를 지나갑니다.

그는 모든 것을 보는 증인으로, 그의 주목을 피하는 것은 없기 때문에 맹세에서 종종 불립니다. 데메테르에게 페르세포네에게 무슨 일이 있었는지 말해준 것도 헬리오스였고, 아프로디테와 아레스의 불륜을 밝힌 것도 그였습니다.""",
    traits_en=["All-seeing", "Radiant", "Eternal", "Witnessing", "Impartial"],
    traits_ko=["모든 것을 보는", "빛나는", "영원한", "목격하는", "공정한"],
    story_en="Helios's son Phaethon begged to drive the sun chariot. Unable to control the divine horses, Phaethon careened across the sky, burning the earth and creating the Sahara desert before Zeus struck him down with a thunderbolt to save the world.",
    story_ko="헬리오스의 아들 파에톤은 태양 전차를 몰게 해달라고 간청했습니다. 신성한 말들을 제어할 수 없어, 파에톤은 하늘을 가로질러 돌진하며, 제우스가 세계를 구하기 위해 벼락으로 그를 쓰러뜨리기 전에 대지를 불태우고 사하라 사막을 만들었습니다.",
    match_message_en="Your features radiate the golden brilliance of Helios. There is an all-seeing quality to your gaze—the look of one who misses nothing and illuminates all they survey.",
    match_message_ko="당신의 이목구비는 헬리오스의 황금빛 광채를 발산합니다. 당신의 눈빛에는 모든 것을 보는 품질이 있습니다—아무것도 놓치지 않고 조망하는 모든 것을 비추는 사람의 모습.",
    image_prompt="Radiant Titan god with golden crown of sun rays, driving golden chariot pulled by fiery horses across the sky, blinding golden light, looking down upon the earth, majestic solar presence",
    visual_description="Radiant golden features, piercing all-seeing eyes, solar crown of light, expression of eternal watchfulness and brilliant power",
    aliases=["Sol", "The All-Seeing"],
    era="Ancient Greece",
    related_characters=["phaethon", "selene", "eos", "apollo"]
)


ASCLEPIUS_DESC = CharacterDescription(
    id="asclepius",
    name_en="Asclepius",
    name_ko="아스클레피오스",
    tagline_en="God of Medicine and Healing",
    tagline_ko="의술과 치유의 신",
    description_en="""Asclepius is the god of medicine and healing, son of Apollo and the mortal Coronis. His skill in medicine became so great that he could even restore the dead to life, making him one of the most beloved figures in Greek mythology.

He learned the healing arts from the wise centaur Chiron and developed them beyond anything the world had seen. His staff, entwined with a single serpent, remains the symbol of medicine to this day.

Zeus struck Asclepius down with a thunderbolt, fearing that his ability to resurrect the dead would upset the natural order. Yet the god of healing was so beloved that Zeus later placed him among the stars and allowed him to continue receiving worship.""",
    description_ko="""아스클레피오스는 의술과 치유의 신으로, 아폴론과 인간 코로니스의 아들입니다. 그의 의술 실력은 너무 뛰어나서 죽은 자도 되살릴 수 있었고, 그를 그리스 신화에서 가장 사랑받는 인물 중 하나로 만들었습니다.

그는 현명한 켄타우로스 케이론에게서 치유의 기술을 배웠고 세상이 본 적 없는 수준으로 발전시켰습니다. 뱀 한 마리가 감긴 그의 지팡이는 오늘날까지 의학의 상징으로 남아 있습니다.

제우스는 죽은 자를 되살리는 그의 능력이 자연의 질서를 어지럽힐까 두려워 벼락으로 아스클레피오스를 쓰러뜨렸습니다. 그러나 치유의 신은 너무나 사랑받았기에 제우스는 나중에 그를 별자리에 올리고 계속 숭배받을 수 있게 허락했습니다.""",
    traits_en=["Healing", "Compassionate", "Skilled", "Devoted", "Gentle"],
    traits_ko=["치유하는", "자비로운", "숙련된", "헌신적인", "온화한"],
    story_en="Asclepius raised Hippolytus from the dead, which angered Hades who complained to Zeus about mortals escaping death. Zeus struck Asclepius with a thunderbolt, but Apollo's grief was so great that Zeus made Asclepius immortal and placed him among the stars as the constellation Ophiuchus.",
    story_ko="아스클레피오스는 히폴리토스를 죽음에서 되살렸고, 이는 인간들이 죽음을 피해가는 것에 대해 제우스에게 불평한 하데스를 화나게 했습니다. 제우스는 벼락으로 아스클레피오스를 쓰러뜨렸지만, 아폴론의 슬픔이 너무 커서 제우스는 아스클레피오스를 불멸로 만들고 뱀주인자리로 별들 사이에 올렸습니다.",
    match_message_en="Your features carry the gentle wisdom of Asclepius. There is a healing presence to your appearance—the look of one who brings comfort and restoration to those in need.",
    match_message_ko="당신의 이목구비는 아스클레피오스의 온화한 지혜를 담고 있습니다. 당신의 외모에는 치유의 존재감이 있습니다—필요한 이들에게 위안과 회복을 가져다주는 사람의 모습.",
    image_prompt="Gentle Greek god in healer's robes, holding staff with serpent coiled around it, surrounded by healing herbs and grateful patients, temple of healing in background, compassionate wise expression, soft golden light",
    visual_description="Gentle wise features, kind compassionate eyes, calm reassuring expression, appearance of someone devoted to helping others",
    aliases=["Aesculapius", "The Healer"],
    era="Ancient Greece",
    related_characters=["apollo", "chiron", "hygeia", "coronis"]
)


# Dictionary of additional Greek descriptions
GREEK_ADDITIONAL_DESCRIPTIONS = {
    "demeter": DEMETER_DESC,
    "hephaestus": HEPHAESTUS_DESC,
    "eros": EROS_DESC,
    "pan": PAN_DESC,
    "prometheus": PROMETHEUS_DESC,
    "hercules": HERCULES_DESC,
    "helios": HELIOS_DESC,
    "asclepius": ASCLEPIUS_DESC,
}

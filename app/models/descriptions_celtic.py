"""
Celtic Mythology Character Descriptions
Contains detailed descriptions for major Celtic mythological figures
"""
from .descriptions import CharacterDescription


DAGDA_DESC = CharacterDescription(
    id="dagda",
    name_en="The Dagda",
    name_ko="다그다",
    tagline_en="The Good God, Father of the Tuatha Dé Danann",
    tagline_ko="선한 신, 투아하 데 다난의 아버지",
    description_en="""The Dagda is the father-figure of the Tuatha Dé Danann, the mythical race of gods in Irish mythology. His name means "The Good God"—not in a moral sense, but meaning he was good at everything: magic, war, wisdom, and craftsmanship.

The Dagda possessed three magical treasures: a cauldron that never emptied, a club that could kill with one end and resurrect with the other, and a harp that could control the seasons and the emotions of all who heard it. He was the archetypal king and druid combined.

Despite his immense power, the Dagda was often depicted with a comical appearance—a short tunic exposing his bottom, and a prodigious appetite. This contrast between power and humility reflects the Celtic love of paradox and the understanding that even gods have human qualities.""",
    description_ko="""다그다는 아일랜드 신화에서 신화적 신들의 종족인 투아하 데 다난의 아버지 같은 인물입니다. 그의 이름은 "선한 신"을 의미하는데—도덕적 의미가 아니라, 마법, 전쟁, 지혜, 기술 등 모든 것에 능숙했다는 뜻입니다.

다그다는 세 가지 마법의 보물을 가졌습니다: 결코 비지 않는 가마솥, 한 끝으로는 죽이고 다른 끝으로는 부활시킬 수 있는 곤봉, 계절과 듣는 모든 이의 감정을 통제할 수 있는 하프. 그는 왕과 드루이드의 전형적인 결합이었습니다.

엄청난 힘에도 불구하고, 다그다는 종종 익살스러운 모습으로 묘사되었습니다—엉덩이가 드러나는 짧은 튜닉과 엄청난 식욕. 이 힘과 겸손 사이의 대조는 역설에 대한 켈트인들의 사랑과 신들도 인간적인 특성을 가지고 있다는 이해를 반영합니다.""",
    traits_en=["Powerful", "Abundant", "Paternal", "Magical", "Paradoxical"],
    traits_ko=["강력한", "풍요로운", "아버지 같은", "마법적인", "역설적인"],
    story_en="Before the Second Battle of Mag Tuired, the Dagda visited the war camp of the Fomorians and was forced to eat a massive pit of porridge. He consumed it all with a ladle as big as two people lying together, then won the battle for his people.",
    story_ko="마그 투어레드의 두 번째 전투 전에, 다그다는 포모리안들의 전쟁 진영을 방문하여 거대한 구덩이의 죽을 먹도록 강요받았습니다. 그는 두 사람이 나란히 누울 만큼 큰 국자로 모든 것을 먹어치운 다음, 그의 백성을 위해 전투에서 승리했습니다.",
    match_message_en="You possess the abundant power of the Dagda. There is a paternal, magical quality to your presence—the look of one who provides endlessly and masters all arts.",
    match_message_ko="당신은 다그다의 풍요로운 힘을 지니고 있습니다. 당신의 존재에는 아버지 같고 마법적인 품질이 있습니다—끝없이 제공하고 모든 기술을 마스터하는 사람의 모습.",
    image_prompt="Massive powerful Celtic god with great club and magical harp, cauldron of plenty, druid's wisdom with warrior's strength, ancient Irish landscape",
    visual_description="Powerful rounded features, wise mirthful eyes, abundant paternal bearing, expression of mastery and generosity",
    aliases=["An Dagda", "Eochaid Ollathair", "Ruad Rofhessa"],
    era="Irish Mythology",
    related_characters=["brigid", "lugh", "morrigan"]
)

BRIGID_DESC = CharacterDescription(
    id="brigid",
    name_en="Brigid",
    name_ko="브리지드",
    tagline_en="Goddess of Fire, Poetry, and Healing",
    tagline_ko="불, 시, 치유의 여신",
    description_en="""Brigid is one of the most beloved goddesses of Celtic Ireland, daughter of the Dagda and patron of poets, healers, and smiths. She represents the creative fire in all its forms—the fire of inspiration, the forge's flame, and the hearth's warmth.

Her importance was so great that she was Christianized as Saint Brigid, with her feast day on February 1st coinciding with the Celtic festival of Imbolc. Many traditions associated with her sacred flame were maintained by Christian nuns at Kildare for centuries.

Brigid was sometimes described as a triple goddess—three sisters all named Brigid, each governing a different domain. She represents the feminine power of creativity, transformation, and nurturing that lies at the heart of Celtic spirituality.""",
    description_ko="""브리지드는 켈트 아일랜드에서 가장 사랑받는 여신 중 하나로, 다그다의 딸이며 시인, 치유자, 대장장이들의 수호자입니다. 그녀는 모든 형태의 창조적 불을 상징합니다—영감의 불, 용광로의 불꽃, 난로의 온기.

그녀의 중요성은 너무 커서 성녀 브리지드로 기독교화되었으며, 그녀의 축일인 2월 1일은 켈트 축제인 임볼크와 일치합니다. 그녀의 신성한 불과 관련된 많은 전통은 킬데어에서 기독교 수녀들에 의해 수세기 동안 유지되었습니다.

브리지드는 때때로 삼중 여신으로 묘사되었습니다—모두 브리지드라는 이름의 세 자매로, 각각 다른 영역을 다스립니다. 그녀는 켈트 영성의 핵심에 있는 창의성, 변형, 양육의 여성적 힘을 상징합니다.""",
    traits_en=["Creative", "Healing", "Inspiring", "Transforming", "Nurturing"],
    traits_ko=["창의적인", "치유하는", "영감을 주는", "변형시키는", "양육하는"],
    story_en="Brigid's sacred flame at Kildare was tended by nineteen nuns, each taking a turn, and on the twentieth night Brigid herself would keep it burning. The flame was never allowed to go out, symbolizing the eternal fire of creativity and spirit.",
    story_ko="킬데어에서 브리지드의 신성한 불은 열아홉 명의 수녀들이 돌아가며 지켰고, 스무 번째 밤에는 브리지드 자신이 그것을 타오르게 유지했습니다. 그 불은 결코 꺼지도록 허용되지 않았으며, 창의성과 정신의 영원한 불을 상징했습니다.",
    match_message_en="You radiate the creative fire of Brigid. There is an inspiring, healing quality to your presence—the look of one who brings warmth and transformation wherever they go.",
    match_message_ko="당신은 브리지드의 창조적 불을 발산합니다. 당신의 존재에는 영감을 주고 치유하는 품질이 있습니다—가는 곳마다 온기와 변화를 가져다주는 사람의 모습.",
    image_prompt="Beautiful Celtic goddess with flame-red hair, holding sacred flame, surrounded by symbols of poetry and smithcraft, gentle yet powerful presence",
    visual_description="Beautiful refined features, bright creative eyes like flames, nurturing yet powerful bearing, expression of creative fire",
    aliases=["Brighid", "Saint Brigid", "Bride"],
    era="Irish Mythology / Early Medieval",
    related_characters=["dagda", "lugh"]
)

LUGH_DESC = CharacterDescription(
    id="lugh",
    name_en="Lugh",
    name_ko="루",
    tagline_en="The Many-Skilled, Sun God and Champion",
    tagline_ko="다재다능한 자, 태양신이자 챔피언",
    description_en="""Lugh Lámhfhada (Lugh of the Long Arm) is the great champion of the Tuatha Dé Danann, master of every art and skill. When he came to Tara seeking to join the gods, he was asked what skill he could offer—and answered that he was master of them all.

Lugh led the Tuatha Dé Danann to victory in the Second Battle of Mag Tuired against the Fomorians. He killed his grandfather Balor of the Evil Eye with a sling stone through his deadly eye, ending the Fomorian threat.

As a sun god, Lugh was celebrated at the harvest festival of Lughnasadh (August 1st), which he created in memory of his foster-mother Tailtiu. His influence spread across Celtic Europe, with the cities of Lyon, Leiden, and London all bearing names derived from his.""",
    description_ko="""루 람파다(긴 팔의 루)는 투아하 데 다난의 위대한 챔피언으로, 모든 예술과 기술의 마스터입니다. 그가 신들에 합류하기 위해 타라에 왔을 때, 어떤 기술을 제공할 수 있는지 물었고—그는 그것들 모두의 마스터라고 대답했습니다.

루는 포모리안들에 맞선 마그 투어레드의 두 번째 전투에서 투아하 데 다난을 승리로 이끌었습니다. 그는 할아버지인 사악한 눈의 발로르를 투석기의 돌로 치명적인 눈을 통해 죽여, 포모리안의 위협을 끝냈습니다.

태양신으로서, 루는 그가 양모인 탈티우를 기념하여 만든 수확 축제인 루나사(8월 1일)에 축하되었습니다. 그의 영향력은 켈트 유럽 전역으로 퍼져, 리옹, 라이덴, 런던 모두 그의 이름에서 파생된 이름을 가지고 있습니다.""",
    traits_en=["Skilled", "Radiant", "Victorious", "Youthful", "Heroic"],
    traits_ko=["숙련된", "빛나는", "승리하는", "젊은", "영웅적인"],
    story_en="When Lugh came to the gates of Tara, the doorkeeper asked his skill. 'I am a smith.' 'We have one.' 'I am a harper.' 'We have one.' This continued until Lugh asked if they had anyone who was all of these at once—and the gates opened.",
    story_ko="루가 타라의 문에 왔을 때, 문지기가 그의 기술을 물었습니다. '나는 대장장이요.' '우리에게 있소.' '나는 하프 연주자요.' '우리에게 있소.' 이것은 루가 이 모든 것을 한꺼번에 하는 사람이 있느냐고 물을 때까지 계속되었고—문이 열렸습니다.",
    match_message_en="You shine with the many skills of Lugh. There is a radiant, heroic quality to your presence—the look of one who masters all arts and leads by excellence.",
    match_message_ko="당신은 루의 다재다능함으로 빛납니다. 당신의 존재에는 빛나고 영웅적인 품질이 있습니다—모든 기술을 마스터하고 뛰어남으로 이끄는 사람의 모습.",
    image_prompt="Radiant Celtic sun god with golden hair and spear of light, master of all arts, youthful heroic beauty, shining with excellence",
    visual_description="Perfect youthful features, bright radiant eyes, heroic confident bearing, expression of mastery and solar brilliance",
    aliases=["Lugh Lámhfhada", "Lug", "Lleu"],
    era="Irish Mythology",
    related_characters=["dagda", "balor", "nuada"]
)

CERNUNNOS_DESC = CharacterDescription(
    id="cernunnos",
    name_en="Cernunnos",
    name_ko="케르눈노스",
    tagline_en="The Horned God, Lord of Wild Things",
    tagline_ko="뿔 달린 신, 야생의 주인",
    description_en="""Cernunnos is the ancient Celtic god of the wild, depicted with the antlers of a stag. His name means "The Horned One," and he represents the untamed forces of nature, the animal kingdom, and the cycle of life and death.

Images of Cernunnos appear on the famous Gundestrup Cauldron, showing him seated in a lotus position surrounded by animals, holding a torc (neck ring) and a serpent. He is often shown as the lord of beasts, connected to fertility, abundance, and the underworld.

As a god of the threshold between civilization and wilderness, Cernunnos represents the primal masculine power that modern society has largely forgotten. He is the wild god of the forest, calling humans to remember their connection to the natural world.""",
    description_ko="""케르눈노스는 수사슴의 뿔을 가진 모습으로 묘사되는 고대 켈트의 야생 신입니다. 그의 이름은 "뿔 달린 자"를 의미하며, 그는 길들여지지 않은 자연의 힘, 동물 왕국, 그리고 생과 사의 순환을 상징합니다.

케르눈노스의 이미지는 유명한 군데스트룹 가마솥에 나타나며, 동물들에 둘러싸여 연꽃 자세로 앉아 토르크(목 고리)와 뱀을 들고 있는 모습을 보여줍니다. 그는 종종 야수들의 주인으로 묘사되며, 다산, 풍요, 그리고 지하세계와 연결됩니다.

문명과 황야 사이의 문턱의 신으로서, 케르눈노스는 현대 사회가 대부분 잊어버린 원시적 남성적 힘을 상징합니다. 그는 숲의 야생 신으로, 인간들에게 자연 세계와의 연결을 기억하라고 부릅니다.""",
    traits_en=["Wild", "Ancient", "Fertile", "Primal", "Connected"],
    traits_ko=["야생적인", "고대의", "비옥한", "원시적인", "연결된"],
    story_en="In ancient times, hunters would pray to Cernunnos before the hunt, asking his blessing and promising to take only what was needed. He was the balance between humanity and the wild, the mediator between the human and animal worlds.",
    story_ko="고대에, 사냥꾼들은 사냥 전에 케르눈노스에게 기도하며, 그의 축복을 구하고 필요한 것만 가져가겠다고 약속했습니다. 그는 인류와 야생 사이의 균형, 인간 세계와 동물 세계 사이의 중재자였습니다.",
    match_message_en="You embody the primal presence of Cernunnos. There is a wild, connected quality to your features—the look of one who understands the untamed forces of nature.",
    match_message_ko="당신은 케르눈노스의 원시적 현존을 구현합니다. 당신의 이목구비에는 야생적이고 연결된 품질이 있습니다—길들여지지 않은 자연의 힘을 이해하는 사람의 모습.",
    image_prompt="Ancient god with great stag antlers, seated among forest animals, holding torc and serpent, primal wisdom in ancient eyes, wild forest background",
    visual_description="Ancient weathered features, deep primal eyes, wild noble bearing, expression of connection to untamed nature",
    aliases=["The Horned God", "Lord of Animals"],
    era="Celtic Antiquity",
    related_characters=["dagda", "morrigan"]
)


# Export dictionary for registry
CELTIC_DESCRIPTIONS: dict[str, CharacterDescription] = {
    "dagda": DAGDA_DESC,
    "brigid": BRIGID_DESC,
    "lugh": LUGH_DESC,
    "cernunnos": CERNUNNOS_DESC,
}

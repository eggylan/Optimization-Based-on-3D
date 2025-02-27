import tkinter as tk#ui界面
from tkinter import filedialog, messagebox, scrolledtext#ui界面
from nbtlib import nbt#加载sche
from BDXConverter import BDX#处理bdx
import re#正则表达计算
import random#随机颜色
from PIL import Image, ImageTk#背景图片


block_names = {"0": "minecraft:air", "16": "minecraft:stone [\"stone_type\"=\"stone\"]",
                 "17": "minecraft:stone [\"stone_type\"=\"granite\"]",
                 "18": "minecraft:stone [\"stone_type\"=\"granite_smooth\"]",
                 "19": "minecraft:stone [\"stone_type\"=\"diorite\"]",
                 "20": "minecraft:stone [\"stone_type\"=\"diorite_smooth\"]",
                 "21": "minecraft:stone [\"stone_type\"=\"andesite\"]",
                 "22": "minecraft:stone [\"stone_type\"=\"andesite_smooth\"]", "32": "minecraft:grass",
                 "48": "minecraft:dirt [\"dirt_type\"=\"normal\"]", "49": "minecraft:dirt [\"dirt_type\"=\"coarse\"]",
                 "50": "minecraft:podzol", "64": "minecraft:cobblestone",
                 "80": "minecraft:planks [\"wood_type\"=\"oak\"]", "81": "minecraft:planks [\"wood_type\"=\"spruce\"]",
                 "82": "minecraft:planks [\"wood_type\"=\"birch\"]",
                 "83": "minecraft:planks [\"wood_type\"=\"jungle\"]",
                 "84": "minecraft:planks [\"wood_type\"=\"acacia\"]",
                 "85": "minecraft:planks [\"wood_type\"=\"dark_oak\"]",
                 "96": "minecraft:sapling [\"age_bit\"=false,\"sapling_type\"=\"oak\"]",
                 "97": "minecraft:sapling [\"age_bit\"=false,\"sapling_type\"=\"spruce\"]",
                 "98": "minecraft:sapling [\"age_bit\"=false,\"sapling_type\"=\"birch\"]",
                 "99": "minecraft:sapling [\"age_bit\"=false,\"sapling_type\"=\"jungle\"]",
                 "100": "minecraft:sapling [\"age_bit\"=false,\"sapling_type\"=\"acacia\"]",
                 "101": "minecraft:sapling [\"age_bit\"=false,\"sapling_type\"=\"dark_oak\"]",
                 "104": "minecraft:sapling [\"age_bit\"=true,\"sapling_type\"=\"oak\"]",
                 "105": "minecraft:sapling [\"age_bit\"=true,\"sapling_type\"=\"spruce\"]",
                 "106": "minecraft:sapling [\"age_bit\"=true,\"sapling_type\"=\"birch\"]",
                 "107": "minecraft:sapling [\"age_bit\"=true,\"sapling_type\"=\"jungle\"]",
                 "108": "minecraft:sapling [\"age_bit\"=true,\"sapling_type\"=\"acacia\"]",
                 "109": "minecraft:sapling [\"age_bit\"=true,\"sapling_type\"=\"dark_oak\"]",
                 "112": "minecraft:bedrock [\"infiniburn_bit\"=false]", "144": "minecraft:water [\"liquid_depth\"=0]",
                 "145": "minecraft:flowing_water [\"liquid_depth\"=1]",
                 "146": "minecraft:flowing_water [\"liquid_depth\"=2]",
                 "147": "minecraft:flowing_water [\"liquid_depth\"=3]",
                 "148": "minecraft:flowing_water [\"liquid_depth\"=4]",
                 "149": "minecraft:flowing_water [\"liquid_depth\"=5]",
                 "150": "minecraft:flowing_water [\"liquid_depth\"=6]",
                 "151": "minecraft:flowing_water [\"liquid_depth\"=7]",
                 "152": "minecraft:flowing_water [\"liquid_depth\"=8]",
                 "153": "minecraft:flowing_water [\"liquid_depth\"=9]",
                 "154": "minecraft:flowing_water [\"liquid_depth\"=10]",
                 "155": "minecraft:flowing_water [\"liquid_depth\"=11]",
                 "156": "minecraft:flowing_water [\"liquid_depth\"=12]",
                 "157": "minecraft:flowing_water [\"liquid_depth\"=13]",
                 "158": "minecraft:flowing_water [\"liquid_depth\"=14]",
                 "159": "minecraft:flowing_water [\"liquid_depth\"=15]", "176": "minecraft:lava [\"liquid_depth\"=0]",
                 "177": "minecraft:flowing_lava [\"liquid_depth\"=1]",
                 "178": "minecraft:flowing_lava [\"liquid_depth\"=2]",
                 "179": "minecraft:flowing_lava [\"liquid_depth\"=3]",
                 "180": "minecraft:flowing_lava [\"liquid_depth\"=4]",
                 "181": "minecraft:flowing_lava [\"liquid_depth\"=5]",
                 "182": "minecraft:flowing_lava [\"liquid_depth\"=6]",
                 "183": "minecraft:flowing_lava [\"liquid_depth\"=7]",
                 "184": "minecraft:flowing_lava [\"liquid_depth\"=8]",
                 "185": "minecraft:flowing_lava [\"liquid_depth\"=9]",
                 "186": "minecraft:flowing_lava [\"liquid_depth\"=10]",
                 "187": "minecraft:flowing_lava [\"liquid_depth\"=11]",
                 "188": "minecraft:flowing_lava [\"liquid_depth\"=12]",
                 "189": "minecraft:flowing_lava [\"liquid_depth\"=13]",
                 "190": "minecraft:flowing_lava [\"liquid_depth\"=14]",
                 "191": "minecraft:flowing_lava [\"liquid_depth\"=15]",
                 "192": "minecraft:sand [\"sand_type\"=\"normal\"]", "193": "minecraft:sand [\"sand_type\"=\"red\"]",
                 "208": "minecraft:gravel", "224": "minecraft:gold_ore", "240": "minecraft:iron_ore",
                 "256": "minecraft:coal_ore", "272": "minecraft:log [\"pillar_axis\"=\"y\",\"old_log_type\"=\"oak\"]",
                 "273": "minecraft:log [\"pillar_axis\"=\"y\",\"old_log_type\"=\"spruce\"]",
                 "274": "minecraft:log [\"pillar_axis\"=\"y\",\"old_log_type\"=\"birch\"]",
                 "275": "minecraft:log [\"pillar_axis\"=\"y\",\"old_log_type\"=\"jungle\"]",
                 "276": "minecraft:log [\"pillar_axis\"=\"x\",\"old_log_type\"=\"oak\"]",
                 "277": "minecraft:log [\"pillar_axis\"=\"x\",\"old_log_type\"=\"spruce\"]",
                 "278": "minecraft:log [\"pillar_axis\"=\"x\",\"old_log_type\"=\"birch\"]",
                 "279": "minecraft:log [\"pillar_axis\"=\"x\",\"old_log_type\"=\"jungle\"]",
                 "280": "minecraft:log [\"pillar_axis\"=\"z\",\"old_log_type\"=\"oak\"]",
                 "281": "minecraft:log [\"pillar_axis\"=\"z\",\"old_log_type\"=\"spruce\"]",
                 "282": "minecraft:log [\"pillar_axis\"=\"z\",\"old_log_type\"=\"birch\"]",
                 "283": "minecraft:log [\"pillar_axis\"=\"z\",\"old_log_type\"=\"jungle\"]",
                 "284": "minecraft:wood [\"stripped_bit\"=false,\"pillar_axis\"=\"y\",\"wood_type\"=\"oak\"]",
                 "285": "minecraft:wood [\"stripped_bit\"=false,\"pillar_axis\"=\"y\",\"wood_type\"=\"spruce\"]",
                 "286": "minecraft:wood [\"stripped_bit\"=false,\"pillar_axis\"=\"y\",\"wood_type\"=\"birch\"]",
                 "287": "minecraft:wood [\"stripped_bit\"=false,\"pillar_axis\"=\"y\",\"wood_type\"=\"jungle\"]",
                 "288": "minecraft:leaves [\"persistent_bit\"=false,\"update_bit\"=false,\"old_leaf_type\"=\"oak\"]",
                 "289": "minecraft:leaves [\"persistent_bit\"=false,\"update_bit\"=false,\"old_leaf_type\"=\"spruce\"]",
                 "290": "minecraft:leaves [\"persistent_bit\"=false,\"update_bit\"=false,\"old_leaf_type\"=\"birch\"]",
                 "291": "minecraft:leaves [\"persistent_bit\"=false,\"update_bit\"=false,\"old_leaf_type\"=\"jungle\"]",
                 "292": "minecraft:leaves [\"persistent_bit\"=true,\"update_bit\"=false,\"old_leaf_type\"=\"oak\"]",
                 "293": "minecraft:leaves [\"persistent_bit\"=true,\"update_bit\"=false,\"old_leaf_type\"=\"spruce\"]",
                 "294": "minecraft:leaves [\"persistent_bit\"=true,\"update_bit\"=false,\"old_leaf_type\"=\"birch\"]",
                 "295": "minecraft:leaves [\"persistent_bit\"=true,\"update_bit\"=false,\"old_leaf_type\"=\"jungle\"]",
                 "296": "minecraft:leaves [\"persistent_bit\"=false,\"update_bit\"=false,\"old_leaf_type\"=\"oak\"]",
                 "297": "minecraft:leaves [\"persistent_bit\"=false,\"update_bit\"=false,\"old_leaf_type\"=\"spruce\"]",
                 "298": "minecraft:leaves [\"persistent_bit\"=false,\"update_bit\"=false,\"old_leaf_type\"=\"birch\"]",
                 "299": "minecraft:leaves [\"persistent_bit\"=false,\"update_bit\"=false,\"old_leaf_type\"=\"jungle\"]",
                 "300": "minecraft:leaves [\"persistent_bit\"=true,\"update_bit\"=false,\"old_leaf_type\"=\"oak\"]",
                 "301": "minecraft:leaves [\"persistent_bit\"=true,\"update_bit\"=false,\"old_leaf_type\"=\"spruce\"]",
                 "302": "minecraft:leaves [\"persistent_bit\"=true,\"update_bit\"=false,\"old_leaf_type\"=\"birch\"]",
                 "303": "minecraft:leaves [\"persistent_bit\"=true,\"update_bit\"=false,\"old_leaf_type\"=\"jungle\"]",
                 "304": "minecraft:sponge [\"sponge_type\"=\"dry\"]",
                 "305": "minecraft:sponge [\"sponge_type\"=\"wet\"]", "320": "minecraft:glass",
                 "336": "minecraft:lapis_ore", "352": "minecraft:lapis_block",
                 "368": "minecraft:dispenser [\"facing_direction\"=0,\"triggered_bit\"=false]",
                 "369": "minecraft:dispenser [\"facing_direction\"=1,\"triggered_bit\"=false]",
                 "370": "minecraft:dispenser [\"facing_direction\"=2,\"triggered_bit\"=false]",
                 "371": "minecraft:dispenser [\"facing_direction\"=3,\"triggered_bit\"=false]",
                 "372": "minecraft:dispenser [\"facing_direction\"=4,\"triggered_bit\"=false]",
                 "373": "minecraft:dispenser [\"facing_direction\"=5,\"triggered_bit\"=false]",
                 "376": "minecraft:dispenser [\"facing_direction\"=0,\"triggered_bit\"=true]",
                 "377": "minecraft:dispenser [\"facing_direction\"=1,\"triggered_bit\"=true]",
                 "378": "minecraft:dispenser [\"facing_direction\"=2,\"triggered_bit\"=true]",
                 "379": "minecraft:dispenser [\"facing_direction\"=3,\"triggered_bit\"=true]",
                 "380": "minecraft:dispenser [\"facing_direction\"=4,\"triggered_bit\"=true]",
                 "381": "minecraft:dispenser [\"facing_direction\"=5,\"triggered_bit\"=true]",
                 "384": "minecraft:sandstone [\"sand_stone_type\"=\"default\"]",
                 "385": "minecraft:sandstone [\"sand_stone_type\"=\"heiroglyphs\"]",
                 "386": "minecraft:sandstone [\"sand_stone_type\"=\"cut\"]", "400": "minecraft:noteblock",
                 "416": "minecraft:bed [\"head_piece_bit\"=false,\"occupied_bit\"=false,\"direction\"=0]",
                 "417": "minecraft:bed [\"head_piece_bit\"=false,\"occupied_bit\"=false,\"direction\"=1]",
                 "418": "minecraft:bed [\"head_piece_bit\"=false,\"occupied_bit\"=false,\"direction\"=2]",
                 "419": "minecraft:bed [\"head_piece_bit\"=false,\"occupied_bit\"=false,\"direction\"=3]",
                 "424": "minecraft:bed [\"head_piece_bit\"=true,\"occupied_bit\"=false,\"direction\"=0]",
                 "425": "minecraft:bed [\"head_piece_bit\"=true,\"occupied_bit\"=false,\"direction\"=1]",
                 "426": "minecraft:bed [\"head_piece_bit\"=true,\"occupied_bit\"=false,\"direction\"=2]",
                 "427": "minecraft:bed [\"head_piece_bit\"=true,\"occupied_bit\"=false,\"direction\"=3]",
                 "428": "minecraft:bed [\"head_piece_bit\"=true,\"occupied_bit\"=true,\"direction\"=0]",
                 "429": "minecraft:bed [\"head_piece_bit\"=true,\"occupied_bit\"=true,\"direction\"=1]",
                 "430": "minecraft:bed [\"head_piece_bit\"=true,\"occupied_bit\"=true,\"direction\"=2]",
                 "431": "minecraft:bed [\"head_piece_bit\"=true,\"occupied_bit\"=true,\"direction\"=3]",
                 "432": "minecraft:golden_rail [\"rail_data_bit\"=false,\"rail_direction\"=0]",
                 "433": "minecraft:golden_rail [\"rail_data_bit\"=false,\"rail_direction\"=1]",
                 "434": "minecraft:golden_rail [\"rail_data_bit\"=false,\"rail_direction\"=2]",
                 "435": "minecraft:golden_rail [\"rail_data_bit\"=false,\"rail_direction\"=3]",
                 "436": "minecraft:golden_rail [\"rail_data_bit\"=false,\"rail_direction\"=4]",
                 "437": "minecraft:golden_rail [\"rail_data_bit\"=false,\"rail_direction\"=5]",
                 "440": "minecraft:golden_rail [\"rail_data_bit\"=true,\"rail_direction\"=0]",
                 "441": "minecraft:golden_rail [\"rail_data_bit\"=true,\"rail_direction\"=1]",
                 "442": "minecraft:golden_rail [\"rail_data_bit\"=true,\"rail_direction\"=2]",
                 "443": "minecraft:golden_rail [\"rail_data_bit\"=true,\"rail_direction\"=3]",
                 "444": "minecraft:golden_rail [\"rail_data_bit\"=true,\"rail_direction\"=4]",
                 "445": "minecraft:golden_rail [\"rail_data_bit\"=true,\"rail_direction\"=5]",
                 "448": "minecraft:detector_rail [\"rail_data_bit\"=false,\"rail_direction\"=0]",
                 "449": "minecraft:detector_rail [\"rail_data_bit\"=false,\"rail_direction\"=1]",
                 "450": "minecraft:detector_rail [\"rail_data_bit\"=false,\"rail_direction\"=2]",
                 "451": "minecraft:detector_rail [\"rail_data_bit\"=false,\"rail_direction\"=3]",
                 "452": "minecraft:detector_rail [\"rail_data_bit\"=false,\"rail_direction\"=4]",
                 "453": "minecraft:detector_rail [\"rail_data_bit\"=false,\"rail_direction\"=5]",
                 "456": "minecraft:detector_rail [\"rail_data_bit\"=true,\"rail_direction\"=0]",
                 "457": "minecraft:detector_rail [\"rail_data_bit\"=true,\"rail_direction\"=1]",
                 "458": "minecraft:detector_rail [\"rail_data_bit\"=true,\"rail_direction\"=2]",
                 "459": "minecraft:detector_rail [\"rail_data_bit\"=true,\"rail_direction\"=3]",
                 "460": "minecraft:detector_rail [\"rail_data_bit\"=true,\"rail_direction\"=4]",
                 "461": "minecraft:detector_rail [\"rail_data_bit\"=true,\"rail_direction\"=5]",
                 "464": "minecraft:sticky_piston [\"facing_direction\"=0]",
                 "465": "minecraft:sticky_piston [\"facing_direction\"=1]",
                 "466": "minecraft:sticky_piston [\"facing_direction\"=3]",
                 "467": "minecraft:sticky_piston [\"facing_direction\"=2]",
                 "468": "minecraft:sticky_piston [\"facing_direction\"=5]",
                 "469": "minecraft:sticky_piston [\"facing_direction\"=4]",
                 "472": "minecraft:sticky_piston [\"facing_direction\"=0]",
                 "473": "minecraft:sticky_piston [\"facing_direction\"=1]",
                 "474": "minecraft:sticky_piston [\"facing_direction\"=3]",
                 "475": "minecraft:sticky_piston [\"facing_direction\"=2]",
                 "476": "minecraft:sticky_piston [\"facing_direction\"=5]",
                 "477": "minecraft:sticky_piston [\"facing_direction\"=4]", "480": "minecraft:web",
                 "497": "minecraft:tallgrass [\"tall_grass_type\"=\"tall\"]",
                 "498": "minecraft:tallgrass [\"tall_grass_type\"=\"fern\"]", "512": "minecraft:deadbush",
                 "528": "minecraft:piston [\"facing_direction\"=0]", "529": "minecraft:piston [\"facing_direction\"=1]",
                 "530": "minecraft:piston [\"facing_direction\"=3]", "531": "minecraft:piston [\"facing_direction\"=2]",
                 "532": "minecraft:piston [\"facing_direction\"=5]", "533": "minecraft:piston [\"facing_direction\"=4]",
                 "536": "minecraft:piston [\"facing_direction\"=0]", "537": "minecraft:piston [\"facing_direction\"=1]",
                 "538": "minecraft:piston [\"facing_direction\"=3]", "539": "minecraft:piston [\"facing_direction\"=2]",
                 "540": "minecraft:piston [\"facing_direction\"=5]", "541": "minecraft:piston [\"facing_direction\"=4]",
                 "544": "minecraft:piston_arm_collision [\"facing_direction\"=0]",
                 "545": "minecraft:piston_arm_collision [\"facing_direction\"=1]",
                 "546": "minecraft:piston_arm_collision [\"facing_direction\"=3]",
                 "547": "minecraft:piston_arm_collision [\"facing_direction\"=2]",
                 "548": "minecraft:piston_arm_collision [\"facing_direction\"=5]",
                 "549": "minecraft:piston_arm_collision [\"facing_direction\"=4]",
                 "552": "minecraft:sticky_piston_arm_collision [\"facing_direction\"=0]",
                 "553": "minecraft:sticky_piston_arm_collision [\"facing_direction\"=1]",
                 "554": "minecraft:sticky_piston_arm_collision [\"facing_direction\"=3]",
                 "555": "minecraft:sticky_piston_arm_collision [\"facing_direction\"=2]",
                 "556": "minecraft:sticky_piston_arm_collision [\"facing_direction\"=5]",
                 "557": "minecraft:sticky_piston_arm_collision [\"facing_direction\"=4]",
                 "560": "minecraft:wool [\"color\"=\"white\"]", "561": "minecraft:wool [\"color\"=\"orange\"]",
                 "562": "minecraft:wool [\"color\"=\"magenta\"]", "563": "minecraft:wool [\"color\"=\"light_blue\"]",
                 "564": "minecraft:wool [\"color\"=\"yellow\"]", "565": "minecraft:wool [\"color\"=\"lime\"]",
                 "566": "minecraft:wool [\"color\"=\"pink\"]", "567": "minecraft:wool [\"color\"=\"gray\"]",
                 "568": "minecraft:wool [\"color\"=\"silver\"]", "569": "minecraft:wool [\"color\"=\"cyan\"]",
                 "570": "minecraft:wool [\"color\"=\"purple\"]", "571": "minecraft:wool [\"color\"=\"blue\"]",
                 "572": "minecraft:wool [\"color\"=\"brown\"]", "573": "minecraft:wool [\"color\"=\"green\"]",
                 "574": "minecraft:wool [\"color\"=\"red\"]", "575": "minecraft:wool [\"color\"=\"black\"]",
                 "576": "minecraft:moving_block", "577": "minecraft:moving_block", "578": "minecraft:moving_block",
                 "579": "minecraft:moving_block", "580": "minecraft:moving_block", "581": "minecraft:moving_block",
                 "584": "minecraft:moving_block", "585": "minecraft:moving_block", "586": "minecraft:moving_block",
                 "587": "minecraft:moving_block", "588": "minecraft:moving_block", "589": "minecraft:moving_block",
                 "592": "minecraft:yellow_flower", "608": "minecraft:red_flower [\"flower_type\"=\"poppy\"]",
                 "609": "minecraft:red_flower [\"flower_type\"=\"orchid\"]",
                 "610": "minecraft:red_flower [\"flower_type\"=\"allium\"]",
                 "611": "minecraft:red_flower [\"flower_type\"=\"houstonia\"]",
                 "612": "minecraft:red_flower [\"flower_type\"=\"tulip_red\"]",
                 "613": "minecraft:red_flower [\"flower_type\"=\"tulip_orange\"]",
                 "614": "minecraft:red_flower [\"flower_type\"=\"tulip_white\"]",
                 "615": "minecraft:red_flower [\"flower_type\"=\"tulip_pink\"]",
                 "616": "minecraft:red_flower [\"flower_type\"=\"oxeye\"]", "624": "minecraft:brown_mushroom",
                 "640": "minecraft:red_mushroom", "656": "minecraft:gold_block", "672": "minecraft:iron_block",
                 "688": "minecraft:double_stone_block_slab4 [\"top_slot_bit\"=false,\"stone_slab_type_4\"=\"stone\"]",
                 "689": "minecraft:double_stone_block_slab [\"stone_slab_type\"=\"sandstone\",\"top_slot_bit\"=false]",
                 "695": "minecraft:double_stone_block_slab [\"stone_slab_type\"=\"quartz\",\"top_slot_bit\"=false]",
                 "696": "minecraft:smooth_stone", "697": "minecraft:sandstone [\"sand_stone_type\"=\"smooth\"]",
                 "698": "minecraft:double_stone_block_slab [\"stone_slab_type\"=\"wood\",\"top_slot_bit\"=false]",
                 "699": "minecraft:double_stone_block_slab [\"stone_slab_type\"=\"cobblestone\",\"top_slot_bit\"=false]",
                 "700": "minecraft:double_stone_block_slab [\"stone_slab_type\"=\"brick\",\"top_slot_bit\"=false]",
                 "701": "minecraft:double_stone_block_slab [\"stone_slab_type\"=\"stone_brick\",\"top_slot_bit\"=false]",
                 "702": "minecraft:double_stone_block_slab [\"stone_slab_type\"=\"nether_brick\",\"top_slot_bit\"=false]",
                 "703": "minecraft:quartz_block [\"chisel_type\"=\"smooth\",\"pillar_axis\"=\"y\"]",
                 "704": "minecraft:stone_block_slab4 [\"top_slot_bit\"=false,\"stone_slab_type_4\"=\"stone\"]",
                 "705": "minecraft:stone_block_slab [\"stone_slab_type\"=\"sandstone\",\"top_slot_bit\"=false]",
                 "706": "minecraft:stone_block_slab [\"stone_slab_type\"=\"wood\",\"top_slot_bit\"=false]",
                 "707": "minecraft:stone_block_slab [\"stone_slab_type\"=\"cobblestone\",\"top_slot_bit\"=false]",
                 "708": "minecraft:stone_block_slab [\"stone_slab_type\"=\"brick\",\"top_slot_bit\"=false]",
                 "709": "minecraft:stone_block_slab [\"stone_slab_type\"=\"stone_brick\",\"top_slot_bit\"=false]",
                 "710": "minecraft:stone_block_slab [\"stone_slab_type\"=\"nether_brick\",\"top_slot_bit\"=false]",
                 "711": "minecraft:stone_block_slab [\"stone_slab_type\"=\"quartz\",\"top_slot_bit\"=false]",
                 "712": "minecraft:stone_block_slab4 [\"top_slot_bit\"=true,\"stone_slab_type_4\"=\"stone\"]",
                 "713": "minecraft:stone_block_slab [\"stone_slab_type\"=\"sandstone\",\"top_slot_bit\"=true]",
                 "714": "minecraft:stone_block_slab [\"stone_slab_type\"=\"wood\",\"top_slot_bit\"=true]",
                 "715": "minecraft:stone_block_slab [\"stone_slab_type\"=\"cobblestone\",\"top_slot_bit\"=true]",
                 "716": "minecraft:stone_block_slab [\"stone_slab_type\"=\"brick\",\"top_slot_bit\"=true]",
                 "717": "minecraft:stone_block_slab [\"stone_slab_type\"=\"stone_brick\",\"top_slot_bit\"=true]",
                 "718": "minecraft:stone_block_slab [\"stone_slab_type\"=\"nether_brick\",\"top_slot_bit\"=true]",
                 "719": "minecraft:stone_block_slab [\"stone_slab_type\"=\"quartz\",\"top_slot_bit\"=true]",
                 "720": "minecraft:brick_block",
                 "737": "minecraft:tnt [\"explode_bit\"=false,\"allow_underwater_bit\"=false]",
                 "752": "minecraft:bookshelf", "768": "minecraft:mossy_cobblestone", "784": "minecraft:obsidian",
                 "801": "minecraft:torch [\"torch_facing_direction\"=\"west\"]",
                 "802": "minecraft:torch [\"torch_facing_direction\"=\"east\"]",
                 "803": "minecraft:torch [\"torch_facing_direction\"=\"north\"]",
                 "804": "minecraft:torch [\"torch_facing_direction\"=\"south\"]",
                 "805": "minecraft:torch [\"torch_facing_direction\"=\"top\"]", "816": "minecraft:fire [\"age\"=0]",
                 "817": "minecraft:fire [\"age\"=1]", "818": "minecraft:fire [\"age\"=2]",
                 "819": "minecraft:fire [\"age\"=3]", "820": "minecraft:fire [\"age\"=4]",
                 "821": "minecraft:fire [\"age\"=5]", "822": "minecraft:fire [\"age\"=6]",
                 "823": "minecraft:fire [\"age\"=7]", "824": "minecraft:fire [\"age\"=8]",
                 "825": "minecraft:fire [\"age\"=9]", "826": "minecraft:fire [\"age\"=10]",
                 "827": "minecraft:fire [\"age\"=11]", "828": "minecraft:fire [\"age\"=12]",
                 "829": "minecraft:fire [\"age\"=13]", "830": "minecraft:fire [\"age\"=14]",
                 "831": "minecraft:fire [\"age\"=15]", "832": "minecraft:mob_spawner",
                 "848": "minecraft:oak_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "849": "minecraft:oak_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "850": "minecraft:oak_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "851": "minecraft:oak_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "852": "minecraft:oak_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "853": "minecraft:oak_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "854": "minecraft:oak_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "855": "minecraft:oak_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "866": "minecraft:chest [\"facing_direction\"=2]", "867": "minecraft:chest [\"facing_direction\"=3]",
                 "868": "minecraft:chest [\"facing_direction\"=4]", "869": "minecraft:chest [\"facing_direction\"=5]",
                 "880": "minecraft:redstone_wire [\"redstone_signal\"=0]",
                 "881": "minecraft:redstone_wire [\"redstone_signal\"=1]",
                 "882": "minecraft:redstone_wire [\"redstone_signal\"=2]",
                 "883": "minecraft:redstone_wire [\"redstone_signal\"=3]",
                 "884": "minecraft:redstone_wire [\"redstone_signal\"=4]",
                 "885": "minecraft:redstone_wire [\"redstone_signal\"=5]",
                 "886": "minecraft:redstone_wire [\"redstone_signal\"=6]",
                 "887": "minecraft:redstone_wire [\"redstone_signal\"=7]",
                 "888": "minecraft:redstone_wire [\"redstone_signal\"=8]",
                 "889": "minecraft:redstone_wire [\"redstone_signal\"=9]",
                 "890": "minecraft:redstone_wire [\"redstone_signal\"=10]",
                 "891": "minecraft:redstone_wire [\"redstone_signal\"=11]",
                 "892": "minecraft:redstone_wire [\"redstone_signal\"=12]",
                 "893": "minecraft:redstone_wire [\"redstone_signal\"=13]",
                 "894": "minecraft:redstone_wire [\"redstone_signal\"=14]",
                 "895": "minecraft:redstone_wire [\"redstone_signal\"=15]", "896": "minecraft:diamond_ore",
                 "912": "minecraft:diamond_block", "928": "minecraft:crafting_table",
                 "944": "minecraft:wheat [\"growth\"=0]", "945": "minecraft:wheat [\"growth\"=1]",
                 "946": "minecraft:wheat [\"growth\"=2]", "947": "minecraft:wheat [\"growth\"=3]",
                 "948": "minecraft:wheat [\"growth\"=4]", "949": "minecraft:wheat [\"growth\"=5]",
                 "950": "minecraft:wheat [\"growth\"=6]", "951": "minecraft:wheat [\"growth\"=7]",
                 "960": "minecraft:farmland [\"moisturized_amount\"=0]",
                 "961": "minecraft:farmland [\"moisturized_amount\"=1]",
                 "962": "minecraft:farmland [\"moisturized_amount\"=2]",
                 "963": "minecraft:farmland [\"moisturized_amount\"=3]",
                 "964": "minecraft:farmland [\"moisturized_amount\"=4]",
                 "965": "minecraft:farmland [\"moisturized_amount\"=5]",
                 "966": "minecraft:farmland [\"moisturized_amount\"=6]",
                 "967": "minecraft:farmland [\"moisturized_amount\"=7]",
                 "978": "minecraft:furnace [\"facing_direction\"=2]",
                 "979": "minecraft:furnace [\"facing_direction\"=3]",
                 "980": "minecraft:furnace [\"facing_direction\"=4]",
                 "981": "minecraft:furnace [\"facing_direction\"=5]",
                 "994": "minecraft:lit_furnace [\"facing_direction\"=2]",
                 "995": "minecraft:lit_furnace [\"facing_direction\"=3]",
                 "996": "minecraft:lit_furnace [\"facing_direction\"=4]",
                 "997": "minecraft:lit_furnace [\"facing_direction\"=5]",
                 "1008": "minecraft:standing_sign [\"ground_sign_direction\"=0]",
                 "1009": "minecraft:standing_sign [\"ground_sign_direction\"=1]",
                 "1010": "minecraft:standing_sign [\"ground_sign_direction\"=2]",
                 "1011": "minecraft:standing_sign [\"ground_sign_direction\"=3]",
                 "1012": "minecraft:standing_sign [\"ground_sign_direction\"=4]",
                 "1013": "minecraft:standing_sign [\"ground_sign_direction\"=5]",
                 "1014": "minecraft:standing_sign [\"ground_sign_direction\"=6]",
                 "1015": "minecraft:standing_sign [\"ground_sign_direction\"=7]",
                 "1016": "minecraft:standing_sign [\"ground_sign_direction\"=8]",
                 "1017": "minecraft:standing_sign [\"ground_sign_direction\"=9]",
                 "1018": "minecraft:standing_sign [\"ground_sign_direction\"=10]",
                 "1019": "minecraft:standing_sign [\"ground_sign_direction\"=11]",
                 "1020": "minecraft:standing_sign [\"ground_sign_direction\"=12]",
                 "1021": "minecraft:standing_sign [\"ground_sign_direction\"=13]",
                 "1022": "minecraft:standing_sign [\"ground_sign_direction\"=14]",
                 "1023": "minecraft:standing_sign [\"ground_sign_direction\"=15]",
                 "1024": "minecraft:wooden_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "1025": "minecraft:wooden_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "1026": "minecraft:wooden_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "1027": "minecraft:wooden_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "1028": "minecraft:wooden_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "1029": "minecraft:wooden_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "1030": "minecraft:wooden_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "1031": "minecraft:wooden_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "1032": "minecraft:wooden_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "1033": "minecraft:wooden_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "1034": "minecraft:wooden_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "1035": "minecraft:wooden_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "1042": "minecraft:ladder [\"facing_direction\"=2]",
                 "1043": "minecraft:ladder [\"facing_direction\"=3]",
                 "1044": "minecraft:ladder [\"facing_direction\"=4]",
                 "1045": "minecraft:ladder [\"facing_direction\"=5]", "1056": "minecraft:rail [\"rail_direction\"=0]",
                 "1057": "minecraft:rail [\"rail_direction\"=1]", "1058": "minecraft:rail [\"rail_direction\"=2]",
                 "1059": "minecraft:rail [\"rail_direction\"=3]", "1060": "minecraft:rail [\"rail_direction\"=4]",
                 "1061": "minecraft:rail [\"rail_direction\"=5]", "1062": "minecraft:rail [\"rail_direction\"=6]",
                 "1063": "minecraft:rail [\"rail_direction\"=7]", "1064": "minecraft:rail [\"rail_direction\"=8]",
                 "1065": "minecraft:rail [\"rail_direction\"=9]",
                 "1072": "minecraft:stone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "1073": "minecraft:stone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "1074": "minecraft:stone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "1075": "minecraft:stone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "1076": "minecraft:stone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "1077": "minecraft:stone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "1078": "minecraft:stone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "1079": "minecraft:stone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "1090": "minecraft:wall_sign [\"facing_direction\"=2]",
                 "1091": "minecraft:wall_sign [\"facing_direction\"=3]",
                 "1092": "minecraft:wall_sign [\"facing_direction\"=4]",
                 "1093": "minecraft:wall_sign [\"facing_direction\"=5]",
                 "1104": "minecraft:lever [\"open_bit\"=false,\"lever_direction\"=\"down_east_west\"]",
                 "1105": "minecraft:lever [\"open_bit\"=false,\"lever_direction\"=\"east\"]",
                 "1106": "minecraft:lever [\"open_bit\"=false,\"lever_direction\"=\"west\"]",
                 "1107": "minecraft:lever [\"open_bit\"=false,\"lever_direction\"=\"south\"]",
                 "1108": "minecraft:lever [\"open_bit\"=false,\"lever_direction\"=\"north\"]",
                 "1109": "minecraft:lever [\"open_bit\"=false,\"lever_direction\"=\"up_north_south\"]",
                 "1110": "minecraft:lever [\"open_bit\"=false,\"lever_direction\"=\"up_east_west\"]",
                 "1111": "minecraft:lever [\"open_bit\"=false,\"lever_direction\"=\"down_north_south\"]",
                 "1112": "minecraft:lever [\"open_bit\"=true,\"lever_direction\"=\"down_east_west\"]",
                 "1113": "minecraft:lever [\"open_bit\"=true,\"lever_direction\"=\"east\"]",
                 "1114": "minecraft:lever [\"open_bit\"=true,\"lever_direction\"=\"west\"]",
                 "1115": "minecraft:lever [\"open_bit\"=true,\"lever_direction\"=\"south\"]",
                 "1116": "minecraft:lever [\"open_bit\"=true,\"lever_direction\"=\"north\"]",
                 "1117": "minecraft:lever [\"open_bit\"=true,\"lever_direction\"=\"up_north_south\"]",
                 "1118": "minecraft:lever [\"open_bit\"=true,\"lever_direction\"=\"up_east_west\"]",
                 "1119": "minecraft:lever [\"open_bit\"=true,\"lever_direction\"=\"down_north_south\"]",
                 "1120": "minecraft:stone_pressure_plate [\"redstone_signal\"=0]",
                 "1121": "minecraft:stone_pressure_plate [\"redstone_signal\"=15]",
                 "1136": "minecraft:iron_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "1137": "minecraft:iron_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "1138": "minecraft:iron_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "1139": "minecraft:iron_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "1140": "minecraft:iron_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "1141": "minecraft:iron_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "1142": "minecraft:iron_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "1143": "minecraft:iron_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "1144": "minecraft:iron_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "1145": "minecraft:iron_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "1146": "minecraft:iron_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "1147": "minecraft:iron_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "1152": "minecraft:wooden_pressure_plate [\"redstone_signal\"=0]",
                 "1153": "minecraft:wooden_pressure_plate [\"redstone_signal\"=15]", "1168": "minecraft:redstone_ore",
                 "1184": "minecraft:lit_redstone_ore",
                 "1201": "minecraft:unlit_redstone_torch [\"torch_facing_direction\"=\"west\"]",
                 "1202": "minecraft:unlit_redstone_torch [\"torch_facing_direction\"=\"east\"]",
                 "1203": "minecraft:unlit_redstone_torch [\"torch_facing_direction\"=\"north\"]",
                 "1204": "minecraft:unlit_redstone_torch [\"torch_facing_direction\"=\"south\"]",
                 "1205": "minecraft:unlit_redstone_torch [\"torch_facing_direction\"=\"top\"]",
                 "1217": "minecraft:redstone_torch [\"torch_facing_direction\"=\"west\"]",
                 "1218": "minecraft:redstone_torch [\"torch_facing_direction\"=\"east\"]",
                 "1219": "minecraft:redstone_torch [\"torch_facing_direction\"=\"north\"]",
                 "1220": "minecraft:redstone_torch [\"torch_facing_direction\"=\"south\"]",
                 "1221": "minecraft:redstone_torch [\"torch_facing_direction\"=\"top\"]",
                 "1232": "minecraft:stone_button [\"facing_direction\"=0,\"button_pressed_bit\"=false]",
                 "1233": "minecraft:stone_button [\"facing_direction\"=5,\"button_pressed_bit\"=false]",
                 "1234": "minecraft:stone_button [\"facing_direction\"=4,\"button_pressed_bit\"=false]",
                 "1235": "minecraft:stone_button [\"facing_direction\"=3,\"button_pressed_bit\"=false]",
                 "1236": "minecraft:stone_button [\"facing_direction\"=2,\"button_pressed_bit\"=false]",
                 "1237": "minecraft:stone_button [\"facing_direction\"=1,\"button_pressed_bit\"=false]",
                 "1240": "minecraft:stone_button [\"facing_direction\"=0,\"button_pressed_bit\"=true]",
                 "1241": "minecraft:stone_button [\"facing_direction\"=5,\"button_pressed_bit\"=true]",
                 "1242": "minecraft:stone_button [\"facing_direction\"=4,\"button_pressed_bit\"=true]",
                 "1243": "minecraft:stone_button [\"facing_direction\"=3,\"button_pressed_bit\"=true]",
                 "1244": "minecraft:stone_button [\"facing_direction\"=2,\"button_pressed_bit\"=true]",
                 "1245": "minecraft:stone_button [\"facing_direction\"=1,\"button_pressed_bit\"=true]",
                 "1248": "minecraft:snow_layer [\"covered_bit\"=false,\"height\"=0]",
                 "1249": "minecraft:snow_layer [\"covered_bit\"=false,\"height\"=1]",
                 "1250": "minecraft:snow_layer [\"covered_bit\"=false,\"height\"=2]",
                 "1251": "minecraft:snow_layer [\"covered_bit\"=false,\"height\"=3]",
                 "1252": "minecraft:snow_layer [\"covered_bit\"=false,\"height\"=4]",
                 "1253": "minecraft:snow_layer [\"covered_bit\"=false,\"height\"=5]",
                 "1254": "minecraft:snow_layer [\"covered_bit\"=false,\"height\"=6]",
                 "1255": "minecraft:snow_layer [\"covered_bit\"=false,\"height\"=7]", "1264": "minecraft:ice",
                 "1280": "minecraft:snow", "1296": "minecraft:cactus [\"age\"=0]",
                 "1297": "minecraft:cactus [\"age\"=1]", "1298": "minecraft:cactus [\"age\"=2]",
                 "1299": "minecraft:cactus [\"age\"=3]", "1300": "minecraft:cactus [\"age\"=4]",
                 "1301": "minecraft:cactus [\"age\"=5]", "1302": "minecraft:cactus [\"age\"=6]",
                 "1303": "minecraft:cactus [\"age\"=7]", "1304": "minecraft:cactus [\"age\"=8]",
                 "1305": "minecraft:cactus [\"age\"=9]", "1306": "minecraft:cactus [\"age\"=10]",
                 "1307": "minecraft:cactus [\"age\"=11]", "1308": "minecraft:cactus [\"age\"=12]",
                 "1309": "minecraft:cactus [\"age\"=13]", "1310": "minecraft:cactus [\"age\"=14]",
                 "1311": "minecraft:cactus [\"age\"=15]", "1312": "minecraft:clay",
                 "1328": "minecraft:reeds [\"age\"=0]", "1329": "minecraft:reeds [\"age\"=1]",
                 "1330": "minecraft:reeds [\"age\"=2]", "1331": "minecraft:reeds [\"age\"=3]",
                 "1332": "minecraft:reeds [\"age\"=4]", "1333": "minecraft:reeds [\"age\"=5]",
                 "1334": "minecraft:reeds [\"age\"=6]", "1335": "minecraft:reeds [\"age\"=7]",
                 "1336": "minecraft:reeds [\"age\"=8]", "1337": "minecraft:reeds [\"age\"=9]",
                 "1338": "minecraft:reeds [\"age\"=10]", "1339": "minecraft:reeds [\"age\"=11]",
                 "1340": "minecraft:reeds [\"age\"=12]", "1341": "minecraft:reeds [\"age\"=13]",
                 "1342": "minecraft:reeds [\"age\"=14]", "1343": "minecraft:reeds [\"age\"=15]",
                 "1344": "minecraft:jukebox", "1345": "minecraft:jukebox",
                 "1360": "minecraft:fence [\"wood_type\"=\"oak\"]",
                 "1376": "minecraft:carved_pumpkin [\"direction\"=0]",
                 "1377": "minecraft:carved_pumpkin [\"direction\"=1]",
                 "1378": "minecraft:carved_pumpkin [\"direction\"=2]",
                 "1379": "minecraft:carved_pumpkin [\"direction\"=3]", "1392": "minecraft:netherrack",
                 "1408": "minecraft:soul_sand", "1424": "minecraft:glowstone",
                 "1441": "minecraft:portal [\"portal_axis\"=\"x\"]", "1442": "minecraft:portal [\"portal_axis\"=\"z\"]",
                 "1456": "minecraft:lit_pumpkin [\"direction\"=0]", "1457": "minecraft:lit_pumpkin [\"direction\"=1]",
                 "1458": "minecraft:lit_pumpkin [\"direction\"=2]", "1459": "minecraft:lit_pumpkin [\"direction\"=3]",
                 "1472": "minecraft:cake [\"bite_counter\"=0]", "1473": "minecraft:cake [\"bite_counter\"=1]",
                 "1474": "minecraft:cake [\"bite_counter\"=2]", "1475": "minecraft:cake [\"bite_counter\"=3]",
                 "1476": "minecraft:cake [\"bite_counter\"=4]", "1477": "minecraft:cake [\"bite_counter\"=5]",
                 "1478": "minecraft:cake [\"bite_counter\"=6]",
                 "1488": "minecraft:unpowered_repeater [\"repeater_delay\"=0,\"direction\"=0]",
                 "1489": "minecraft:unpowered_repeater [\"repeater_delay\"=0,\"direction\"=1]",
                 "1490": "minecraft:unpowered_repeater [\"repeater_delay\"=0,\"direction\"=2]",
                 "1491": "minecraft:unpowered_repeater [\"repeater_delay\"=0,\"direction\"=3]",
                 "1492": "minecraft:unpowered_repeater [\"repeater_delay\"=1,\"direction\"=0]",
                 "1493": "minecraft:unpowered_repeater [\"repeater_delay\"=1,\"direction\"=1]",
                 "1494": "minecraft:unpowered_repeater [\"repeater_delay\"=1,\"direction\"=2]",
                 "1495": "minecraft:unpowered_repeater [\"repeater_delay\"=1,\"direction\"=3]",
                 "1496": "minecraft:unpowered_repeater [\"repeater_delay\"=2,\"direction\"=0]",
                 "1497": "minecraft:unpowered_repeater [\"repeater_delay\"=2,\"direction\"=1]",
                 "1498": "minecraft:unpowered_repeater [\"repeater_delay\"=2,\"direction\"=2]",
                 "1499": "minecraft:unpowered_repeater [\"repeater_delay\"=2,\"direction\"=3]",
                 "1500": "minecraft:unpowered_repeater [\"repeater_delay\"=3,\"direction\"=0]",
                 "1501": "minecraft:unpowered_repeater [\"repeater_delay\"=3,\"direction\"=1]",
                 "1502": "minecraft:unpowered_repeater [\"repeater_delay\"=3,\"direction\"=2]",
                 "1503": "minecraft:unpowered_repeater [\"repeater_delay\"=3,\"direction\"=3]",
                 "1504": "minecraft:powered_repeater [\"repeater_delay\"=0,\"direction\"=0]",
                 "1505": "minecraft:powered_repeater [\"repeater_delay\"=0,\"direction\"=1]",
                 "1506": "minecraft:powered_repeater [\"repeater_delay\"=0,\"direction\"=2]",
                 "1507": "minecraft:powered_repeater [\"repeater_delay\"=0,\"direction\"=3]",
                 "1508": "minecraft:powered_repeater [\"repeater_delay\"=1,\"direction\"=0]",
                 "1509": "minecraft:powered_repeater [\"repeater_delay\"=1,\"direction\"=1]",
                 "1510": "minecraft:powered_repeater [\"repeater_delay\"=1,\"direction\"=2]",
                 "1511": "minecraft:powered_repeater [\"repeater_delay\"=1,\"direction\"=3]",
                 "1512": "minecraft:powered_repeater [\"repeater_delay\"=2,\"direction\"=0]",
                 "1513": "minecraft:powered_repeater [\"repeater_delay\"=2,\"direction\"=1]",
                 "1514": "minecraft:powered_repeater [\"repeater_delay\"=2,\"direction\"=2]",
                 "1515": "minecraft:powered_repeater [\"repeater_delay\"=2,\"direction\"=3]",
                 "1516": "minecraft:powered_repeater [\"repeater_delay\"=3,\"direction\"=0]",
                 "1517": "minecraft:powered_repeater [\"repeater_delay\"=3,\"direction\"=1]",
                 "1518": "minecraft:powered_repeater [\"repeater_delay\"=3,\"direction\"=2]",
                 "1519": "minecraft:powered_repeater [\"repeater_delay\"=3,\"direction\"=3]",
                 "1520": "minecraft:stained_glass [\"color\"=\"white\"]",
                 "1521": "minecraft:stained_glass [\"color\"=\"orange\"]",
                 "1522": "minecraft:stained_glass [\"color\"=\"magenta\"]",
                 "1523": "minecraft:stained_glass [\"color\"=\"light_blue\"]",
                 "1524": "minecraft:stained_glass [\"color\"=\"yellow\"]",
                 "1525": "minecraft:stained_glass [\"color\"=\"lime\"]",
                 "1526": "minecraft:stained_glass [\"color\"=\"pink\"]",
                 "1527": "minecraft:stained_glass [\"color\"=\"gray\"]",
                 "1528": "minecraft:stained_glass [\"color\"=\"silver\"]",
                 "1529": "minecraft:stained_glass [\"color\"=\"cyan\"]",
                 "1530": "minecraft:stained_glass [\"color\"=\"purple\"]",
                 "1531": "minecraft:stained_glass [\"color\"=\"blue\"]",
                 "1532": "minecraft:stained_glass [\"color\"=\"brown\"]",
                 "1533": "minecraft:stained_glass [\"color\"=\"green\"]",
                 "1534": "minecraft:stained_glass [\"color\"=\"red\"]",
                 "1535": "minecraft:stained_glass [\"color\"=\"black\"]",
                 "1536": "minecraft:trapdoor [\"open_bit\"=false,\"upside_down_bit\"=false,\"direction\"=3]",
                 "1537": "minecraft:trapdoor [\"open_bit\"=false,\"upside_down_bit\"=false,\"direction\"=2]",
                 "1538": "minecraft:trapdoor [\"open_bit\"=false,\"upside_down_bit\"=false,\"direction\"=1]",
                 "1539": "minecraft:trapdoor [\"open_bit\"=false,\"upside_down_bit\"=false,\"direction\"=0]",
                 "1540": "minecraft:trapdoor [\"open_bit\"=true,\"upside_down_bit\"=false,\"direction\"=3]",
                 "1541": "minecraft:trapdoor [\"open_bit\"=true,\"upside_down_bit\"=false,\"direction\"=2]",
                 "1542": "minecraft:trapdoor [\"open_bit\"=true,\"upside_down_bit\"=false,\"direction\"=1]",
                 "1543": "minecraft:trapdoor [\"open_bit\"=true,\"upside_down_bit\"=false,\"direction\"=0]",
                 "1544": "minecraft:trapdoor [\"open_bit\"=false,\"upside_down_bit\"=true,\"direction\"=3]",
                 "1545": "minecraft:trapdoor [\"open_bit\"=false,\"upside_down_bit\"=true,\"direction\"=2]",
                 "1546": "minecraft:trapdoor [\"open_bit\"=false,\"upside_down_bit\"=true,\"direction\"=1]",
                 "1547": "minecraft:trapdoor [\"open_bit\"=false,\"upside_down_bit\"=true,\"direction\"=0]",
                 "1548": "minecraft:trapdoor [\"open_bit\"=true,\"upside_down_bit\"=true,\"direction\"=3]",
                 "1549": "minecraft:trapdoor [\"open_bit\"=true,\"upside_down_bit\"=true,\"direction\"=2]",
                 "1550": "minecraft:trapdoor [\"open_bit\"=true,\"upside_down_bit\"=true,\"direction\"=1]",
                 "1551": "minecraft:trapdoor [\"open_bit\"=true,\"upside_down_bit\"=true,\"direction\"=0]",
                 "1552": "minecraft:monster_egg [\"monster_egg_stone_type\"=\"stone\"]",
                 "1553": "minecraft:monster_egg [\"monster_egg_stone_type\"=\"cobblestone\"]",
                 "1554": "minecraft:monster_egg [\"monster_egg_stone_type\"=\"stone_brick\"]",
                 "1555": "minecraft:monster_egg [\"monster_egg_stone_type\"=\"mossy_stone_brick\"]",
                 "1556": "minecraft:monster_egg [\"monster_egg_stone_type\"=\"cracked_stone_brick\"]",
                 "1557": "minecraft:monster_egg [\"monster_egg_stone_type\"=\"chiseled_stone_brick\"]",
                 "1568": "minecraft:stonebrick [\"stone_brick_type\"=\"default\"]",
                 "1569": "minecraft:stonebrick [\"stone_brick_type\"=\"mossy\"]",
                 "1570": "minecraft:stonebrick [\"stone_brick_type\"=\"cracked\"]",
                 "1571": "minecraft:stonebrick [\"stone_brick_type\"=\"chiseled\"]",
                 "1585": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=1]",
                 "1586": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=2]",
                 "1587": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=3]",
                 "1588": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=4]",
                 "1589": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=5]",
                 "1590": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=6]",
                 "1591": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=7]",
                 "1592": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=8]",
                 "1593": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=9]",
                 "1597": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=0]",
                 "1598": "minecraft:brown_mushroom_block [\"huge_mushroom_bits\"=0]",
                 "1601": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=1]",
                 "1602": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=2]",
                 "1603": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=3]",
                 "1604": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=4]",
                 "1605": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=5]",
                 "1606": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=6]",
                 "1607": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=7]",
                 "1608": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=8]",
                 "1609": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=9]",
                 "1610": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=15]",
                 "1613": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=0]",
                 "1614": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=0]",
                 "1615": "minecraft:red_mushroom_block [\"huge_mushroom_bits\"=15]", "1616": "minecraft:iron_bars",
                 "1632": "minecraft:glass_pane", "1648": "minecraft:melon_block",
                 "1664": "minecraft:pumpkin_stem [\"growth\"=0,\"facing_direction\"=0]",
                 "1665": "minecraft:pumpkin_stem [\"growth\"=1,\"facing_direction\"=0]",
                 "1666": "minecraft:pumpkin_stem [\"growth\"=2,\"facing_direction\"=0]",
                 "1667": "minecraft:pumpkin_stem [\"growth\"=3,\"facing_direction\"=0]",
                 "1668": "minecraft:pumpkin_stem [\"growth\"=4,\"facing_direction\"=0]",
                 "1669": "minecraft:pumpkin_stem [\"growth\"=5,\"facing_direction\"=0]",
                 "1670": "minecraft:pumpkin_stem [\"growth\"=6,\"facing_direction\"=0]",
                 "1671": "minecraft:pumpkin_stem [\"growth\"=7,\"facing_direction\"=0]",
                 "1680": "minecraft:melon_stem [\"growth\"=0,\"facing_direction\"=0]",
                 "1681": "minecraft:melon_stem [\"growth\"=1,\"facing_direction\"=0]",
                 "1682": "minecraft:melon_stem [\"growth\"=2,\"facing_direction\"=0]",
                 "1683": "minecraft:melon_stem [\"growth\"=3,\"facing_direction\"=0]",
                 "1684": "minecraft:melon_stem [\"growth\"=4,\"facing_direction\"=0]",
                 "1685": "minecraft:melon_stem [\"growth\"=5,\"facing_direction\"=0]",
                 "1686": "minecraft:melon_stem [\"growth\"=6,\"facing_direction\"=0]",
                 "1687": "minecraft:melon_stem [\"growth\"=7,\"facing_direction\"=0]",
                 "1696": "minecraft:vine [\"vine_direction_bits\"=0]",
                 "1697": "minecraft:vine [\"vine_direction_bits\"=1]",
                 "1698": "minecraft:vine [\"vine_direction_bits\"=2]",
                 "1699": "minecraft:vine [\"vine_direction_bits\"=3]",
                 "1700": "minecraft:vine [\"vine_direction_bits\"=4]",
                 "1701": "minecraft:vine [\"vine_direction_bits\"=5]",
                 "1702": "minecraft:vine [\"vine_direction_bits\"=6]",
                 "1703": "minecraft:vine [\"vine_direction_bits\"=7]",
                 "1704": "minecraft:vine [\"vine_direction_bits\"=8]",
                 "1705": "minecraft:vine [\"vine_direction_bits\"=9]",
                 "1706": "minecraft:vine [\"vine_direction_bits\"=10]",
                 "1707": "minecraft:vine [\"vine_direction_bits\"=11]",
                 "1708": "minecraft:vine [\"vine_direction_bits\"=12]",
                 "1709": "minecraft:vine [\"vine_direction_bits\"=13]",
                 "1710": "minecraft:vine [\"vine_direction_bits\"=14]",
                 "1711": "minecraft:vine [\"vine_direction_bits\"=15]",
                 "1712": "minecraft:fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "1713": "minecraft:fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "1714": "minecraft:fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "1715": "minecraft:fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "1716": "minecraft:fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "1717": "minecraft:fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "1718": "minecraft:fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "1719": "minecraft:fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "1720": "minecraft:fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "1721": "minecraft:fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "1722": "minecraft:fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "1723": "minecraft:fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "1724": "minecraft:fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "1725": "minecraft:fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "1726": "minecraft:fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "1727": "minecraft:fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "1728": "minecraft:brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "1729": "minecraft:brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "1730": "minecraft:brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "1731": "minecraft:brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "1732": "minecraft:brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "1733": "minecraft:brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "1734": "minecraft:brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "1735": "minecraft:brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "1744": "minecraft:stone_brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "1745": "minecraft:stone_brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "1746": "minecraft:stone_brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "1747": "minecraft:stone_brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "1748": "minecraft:stone_brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "1749": "minecraft:stone_brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "1750": "minecraft:stone_brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "1751": "minecraft:stone_brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "1760": "minecraft:mycelium", "1776": "minecraft:waterlily", "1792": "minecraft:nether_brick",
                 "1808": "minecraft:nether_brick_fence",
                 "1824": "minecraft:nether_brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "1825": "minecraft:nether_brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "1826": "minecraft:nether_brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "1827": "minecraft:nether_brick_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "1828": "minecraft:nether_brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "1829": "minecraft:nether_brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "1830": "minecraft:nether_brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "1831": "minecraft:nether_brick_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "1840": "minecraft:nether_wart [\"age\"=0]", "1841": "minecraft:nether_wart [\"age\"=1]",
                 "1842": "minecraft:nether_wart [\"age\"=2]", "1843": "minecraft:nether_wart [\"age\"=3]",
                 "1856": "minecraft:enchanting_table",
                 "1872": "minecraft:brewing_stand [\"brewing_stand_slot_c_bit\"=false,\"brewing_stand_slot_a_bit\"=false,\"brewing_stand_slot_b_bit\"=false]",
                 "1873": "minecraft:brewing_stand [\"brewing_stand_slot_c_bit\"=false,\"brewing_stand_slot_a_bit\"=true,\"brewing_stand_slot_b_bit\"=false]",
                 "1874": "minecraft:brewing_stand [\"brewing_stand_slot_c_bit\"=false,\"brewing_stand_slot_a_bit\"=false,\"brewing_stand_slot_b_bit\"=true]",
                 "1875": "minecraft:brewing_stand [\"brewing_stand_slot_c_bit\"=false,\"brewing_stand_slot_a_bit\"=true,\"brewing_stand_slot_b_bit\"=true]",
                 "1876": "minecraft:brewing_stand [\"brewing_stand_slot_c_bit\"=true,\"brewing_stand_slot_a_bit\"=false,\"brewing_stand_slot_b_bit\"=false]",
                 "1877": "minecraft:brewing_stand [\"brewing_stand_slot_c_bit\"=true,\"brewing_stand_slot_a_bit\"=true,\"brewing_stand_slot_b_bit\"=false]",
                 "1878": "minecraft:brewing_stand [\"brewing_stand_slot_c_bit\"=true,\"brewing_stand_slot_a_bit\"=false,\"brewing_stand_slot_b_bit\"=true]",
                 "1879": "minecraft:brewing_stand [\"brewing_stand_slot_c_bit\"=true,\"brewing_stand_slot_a_bit\"=true,\"brewing_stand_slot_b_bit\"=true]",
                 "1888": "minecraft:cauldron [\"cauldron_liquid\"=\"water\",\"fill_level\"=0]",
                 "1889": "minecraft:cauldron [\"cauldron_liquid\"=\"water\",\"fill_level\"=3]",
                 "1890": "minecraft:cauldron [\"cauldron_liquid\"=\"water\",\"fill_level\"=4]",
                 "1891": "minecraft:cauldron [\"cauldron_liquid\"=\"water\",\"fill_level\"=6]",
                 "1904": "minecraft:end_portal",
                 "1920": "minecraft:end_portal_frame [\"end_portal_eye_bit\"=false,\"direction\"=0]",
                 "1921": "minecraft:end_portal_frame [\"end_portal_eye_bit\"=false,\"direction\"=1]",
                 "1922": "minecraft:end_portal_frame [\"end_portal_eye_bit\"=false,\"direction\"=2]",
                 "1923": "minecraft:end_portal_frame [\"end_portal_eye_bit\"=false,\"direction\"=3]",
                 "1924": "minecraft:end_portal_frame [\"end_portal_eye_bit\"=true,\"direction\"=0]",
                 "1925": "minecraft:end_portal_frame [\"end_portal_eye_bit\"=true,\"direction\"=1]",
                 "1926": "minecraft:end_portal_frame [\"end_portal_eye_bit\"=true,\"direction\"=2]",
                 "1927": "minecraft:end_portal_frame [\"end_portal_eye_bit\"=true,\"direction\"=3]",
                 "1936": "minecraft:end_stone", "1952": "minecraft:dragon_egg", "1968": "minecraft:redstone_lamp",
                 "1984": "minecraft:lit_redstone_lamp",
                 "2000": "minecraft:double_wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"oak\"]",
                 "2001": "minecraft:double_wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"spruce\"]",
                 "2002": "minecraft:double_wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"birch\"]",
                 "2003": "minecraft:double_wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"jungle\"]",
                 "2004": "minecraft:double_wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"acacia\"]",
                 "2005": "minecraft:double_wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"dark_oak\"]",
                 "2016": "minecraft:wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"oak\"]",
                 "2017": "minecraft:wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"spruce\"]",
                 "2018": "minecraft:wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"birch\"]",
                 "2019": "minecraft:wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"jungle\"]",
                 "2020": "minecraft:wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"acacia\"]",
                 "2021": "minecraft:wooden_slab [\"top_slot_bit\"=false,\"wood_type\"=\"dark_oak\"]",
                 "2024": "minecraft:wooden_slab [\"top_slot_bit\"=true,\"wood_type\"=\"oak\"]",
                 "2025": "minecraft:wooden_slab [\"top_slot_bit\"=true,\"wood_type\"=\"spruce\"]",
                 "2026": "minecraft:wooden_slab [\"top_slot_bit\"=true,\"wood_type\"=\"birch\"]",
                 "2027": "minecraft:wooden_slab [\"top_slot_bit\"=true,\"wood_type\"=\"jungle\"]",
                 "2028": "minecraft:wooden_slab [\"top_slot_bit\"=true,\"wood_type\"=\"acacia\"]",
                 "2029": "minecraft:wooden_slab [\"top_slot_bit\"=true,\"wood_type\"=\"dark_oak\"]",
                 "2032": "minecraft:cocoa [\"age\"=0,\"direction\"=0]",
                 "2033": "minecraft:cocoa [\"age\"=0,\"direction\"=1]",
                 "2034": "minecraft:cocoa [\"age\"=0,\"direction\"=2]",
                 "2035": "minecraft:cocoa [\"age\"=0,\"direction\"=3]",
                 "2036": "minecraft:cocoa [\"age\"=1,\"direction\"=0]",
                 "2037": "minecraft:cocoa [\"age\"=1,\"direction\"=1]",
                 "2038": "minecraft:cocoa [\"age\"=1,\"direction\"=2]",
                 "2039": "minecraft:cocoa [\"age\"=1,\"direction\"=3]",
                 "2040": "minecraft:cocoa [\"age\"=2,\"direction\"=0]",
                 "2041": "minecraft:cocoa [\"age\"=2,\"direction\"=1]",
                 "2042": "minecraft:cocoa [\"age\"=2,\"direction\"=2]",
                 "2043": "minecraft:cocoa [\"age\"=2,\"direction\"=3]",
                 "2048": "minecraft:sandstone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "2049": "minecraft:sandstone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "2050": "minecraft:sandstone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "2051": "minecraft:sandstone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "2052": "minecraft:sandstone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "2053": "minecraft:sandstone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "2054": "minecraft:sandstone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "2055": "minecraft:sandstone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "2064": "minecraft:emerald_ore", "2082": "minecraft:ender_chest [\"facing_direction\"=2]",
                 "2083": "minecraft:ender_chest [\"facing_direction\"=3]",
                 "2084": "minecraft:ender_chest [\"facing_direction\"=4]",
                 "2085": "minecraft:ender_chest [\"facing_direction\"=5]",
                 "2096": "minecraft:tripwire_hook [\"powered_bit\"=false,\"attached_bit\"=false,\"direction\"=0]",
                 "2097": "minecraft:tripwire_hook [\"powered_bit\"=false,\"attached_bit\"=false,\"direction\"=1]",
                 "2098": "minecraft:tripwire_hook [\"powered_bit\"=false,\"attached_bit\"=false,\"direction\"=2]",
                 "2099": "minecraft:tripwire_hook [\"powered_bit\"=false,\"attached_bit\"=false,\"direction\"=3]",
                 "2100": "minecraft:tripwire_hook [\"powered_bit\"=false,\"attached_bit\"=true,\"direction\"=0]",
                 "2101": "minecraft:tripwire_hook [\"powered_bit\"=false,\"attached_bit\"=true,\"direction\"=1]",
                 "2102": "minecraft:tripwire_hook [\"powered_bit\"=false,\"attached_bit\"=true,\"direction\"=2]",
                 "2103": "minecraft:tripwire_hook [\"powered_bit\"=false,\"attached_bit\"=true,\"direction\"=3]",
                 "2104": "minecraft:tripwire_hook [\"powered_bit\"=true,\"attached_bit\"=false,\"direction\"=0]",
                 "2105": "minecraft:tripwire_hook [\"powered_bit\"=true,\"attached_bit\"=false,\"direction\"=1]",
                 "2106": "minecraft:tripwire_hook [\"powered_bit\"=true,\"attached_bit\"=false,\"direction\"=2]",
                 "2107": "minecraft:tripwire_hook [\"powered_bit\"=true,\"attached_bit\"=false,\"direction\"=3]",
                 "2108": "minecraft:tripwire_hook [\"powered_bit\"=true,\"attached_bit\"=true,\"direction\"=0]",
                 "2109": "minecraft:tripwire_hook [\"powered_bit\"=true,\"attached_bit\"=true,\"direction\"=1]",
                 "2110": "minecraft:tripwire_hook [\"powered_bit\"=true,\"attached_bit\"=true,\"direction\"=2]",
                 "2111": "minecraft:tripwire_hook [\"powered_bit\"=true,\"attached_bit\"=true,\"direction\"=3]",
                 "2114": "minecraft:trip_wire [\"powered_bit\"=false,\"suspended_bit\"=true,\"disarmed_bit\"=false,\"attached_bit\"=false]",
                 "2115": "minecraft:trip_wire [\"powered_bit\"=true,\"suspended_bit\"=true,\"disarmed_bit\"=false,\"attached_bit\"=false]",
                 "2118": "minecraft:trip_wire [\"powered_bit\"=false,\"suspended_bit\"=true,\"disarmed_bit\"=false,\"attached_bit\"=true]",
                 "2119": "minecraft:trip_wire [\"powered_bit\"=true,\"suspended_bit\"=true,\"disarmed_bit\"=false,\"attached_bit\"=true]",
                 "2122": "minecraft:trip_wire [\"powered_bit\"=false,\"suspended_bit\"=true,\"disarmed_bit\"=true,\"attached_bit\"=false]",
                 "2123": "minecraft:trip_wire [\"powered_bit\"=true,\"suspended_bit\"=true,\"disarmed_bit\"=true,\"attached_bit\"=false]",
                 "2125": "minecraft:trip_wire [\"powered_bit\"=true,\"suspended_bit\"=true,\"disarmed_bit\"=true,\"attached_bit\"=true]",
                 "2126": "minecraft:trip_wire [\"powered_bit\"=false,\"suspended_bit\"=true,\"disarmed_bit\"=true,\"attached_bit\"=true]",
                 "2128": "minecraft:emerald_block",
                 "2144": "minecraft:spruce_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "2145": "minecraft:spruce_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "2146": "minecraft:spruce_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "2147": "minecraft:spruce_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "2148": "minecraft:spruce_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "2149": "minecraft:spruce_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "2150": "minecraft:spruce_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "2151": "minecraft:spruce_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "2160": "minecraft:birch_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "2161": "minecraft:birch_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "2162": "minecraft:birch_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "2163": "minecraft:birch_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "2164": "minecraft:birch_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "2165": "minecraft:birch_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "2166": "minecraft:birch_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "2167": "minecraft:birch_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "2176": "minecraft:jungle_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "2177": "minecraft:jungle_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "2178": "minecraft:jungle_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "2179": "minecraft:jungle_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "2180": "minecraft:jungle_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "2181": "minecraft:jungle_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "2182": "minecraft:jungle_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "2183": "minecraft:jungle_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "2192": "minecraft:command_block [\"conditional_bit\"=false,\"facing_direction\"=0]",
                 "2193": "minecraft:command_block [\"conditional_bit\"=false,\"facing_direction\"=1]",
                 "2194": "minecraft:command_block [\"conditional_bit\"=false,\"facing_direction\"=2]",
                 "2195": "minecraft:command_block [\"conditional_bit\"=false,\"facing_direction\"=3]",
                 "2196": "minecraft:command_block [\"conditional_bit\"=false,\"facing_direction\"=4]",
                 "2197": "minecraft:command_block [\"conditional_bit\"=false,\"facing_direction\"=5]",
                 "2200": "minecraft:command_block [\"conditional_bit\"=true,\"facing_direction\"=0]",
                 "2201": "minecraft:command_block [\"conditional_bit\"=true,\"facing_direction\"=1]",
                 "2202": "minecraft:command_block [\"conditional_bit\"=true,\"facing_direction\"=2]",
                 "2203": "minecraft:command_block [\"conditional_bit\"=true,\"facing_direction\"=3]",
                 "2204": "minecraft:command_block [\"conditional_bit\"=true,\"facing_direction\"=4]",
                 "2205": "minecraft:command_block [\"conditional_bit\"=true,\"facing_direction\"=5]",
                 "2208": "minecraft:beacon",
                 "2224": "minecraft:cobblestone_wall [\"wall_connection_type_east\"=\"none\",\"wall_post_bit\"=true,\"wall_connection_type_south\"=\"none\",\"wall_connection_type_west\"=\"none\",\"wall_connection_type_north\"=\"none\",\"wall_block_type\"=\"cobblestone\"]",
                 "2225": "minecraft:cobblestone_wall [\"wall_connection_type_east\"=\"none\",\"wall_connection_type_north\"=\"none\",\"wall_connection_type_south\"=\"none\",\"wall_connection_type_west\"=\"none\",\"wall_post_bit\"=true,\"wall_block_type\"=\"mossy_cobblestone\"]",
                 "2255": "minecraft:flower_pot [\"update_bit\"=false]", "2256": "minecraft:carrots [\"growth\"=0]",
                 "2257": "minecraft:carrots [\"growth\"=1]", "2258": "minecraft:carrots [\"growth\"=2]",
                 "2259": "minecraft:carrots [\"growth\"=3]", "2260": "minecraft:carrots [\"growth\"=4]",
                 "2261": "minecraft:carrots [\"growth\"=5]", "2262": "minecraft:carrots [\"growth\"=6]",
                 "2263": "minecraft:carrots [\"growth\"=7]", "2272": "minecraft:potatoes [\"growth\"=0]",
                 "2273": "minecraft:potatoes [\"growth\"=1]", "2274": "minecraft:potatoes [\"growth\"=2]",
                 "2275": "minecraft:potatoes [\"growth\"=3]", "2276": "minecraft:potatoes [\"growth\"=4]",
                 "2277": "minecraft:potatoes [\"growth\"=5]", "2278": "minecraft:potatoes [\"growth\"=6]",
                 "2279": "minecraft:potatoes [\"growth\"=7]",
                 "2288": "minecraft:wooden_button [\"facing_direction\"=0,\"button_pressed_bit\"=false]",
                 "2289": "minecraft:wooden_button [\"facing_direction\"=5,\"button_pressed_bit\"=false]",
                 "2290": "minecraft:wooden_button [\"facing_direction\"=4,\"button_pressed_bit\"=false]",
                 "2291": "minecraft:wooden_button [\"facing_direction\"=3,\"button_pressed_bit\"=false]",
                 "2292": "minecraft:wooden_button [\"facing_direction\"=2,\"button_pressed_bit\"=false]",
                 "2293": "minecraft:wooden_button [\"facing_direction\"=1,\"button_pressed_bit\"=false]",
                 "2296": "minecraft:wooden_button [\"facing_direction\"=0,\"button_pressed_bit\"=true]",
                 "2297": "minecraft:wooden_button [\"facing_direction\"=5,\"button_pressed_bit\"=true]",
                 "2298": "minecraft:wooden_button [\"facing_direction\"=4,\"button_pressed_bit\"=true]",
                 "2299": "minecraft:wooden_button [\"facing_direction\"=3,\"button_pressed_bit\"=true]",
                 "2300": "minecraft:wooden_button [\"facing_direction\"=2,\"button_pressed_bit\"=true]",
                 "2301": "minecraft:wooden_button [\"facing_direction\"=1,\"button_pressed_bit\"=true]",
                 "2313": "minecraft:skull [\"facing_direction\"=1]", "2314": "minecraft:skull [\"facing_direction\"=2]",
                 "2315": "minecraft:skull [\"facing_direction\"=3]", "2316": "minecraft:skull [\"facing_direction\"=4]",
                 "2317": "minecraft:skull [\"facing_direction\"=5]",
                 "2320": "minecraft:anvil [\"damage\"=\"undamaged\",\"direction\"=0]",
                 "2321": "minecraft:anvil [\"damage\"=\"undamaged\",\"direction\"=1]",
                 "2322": "minecraft:anvil [\"damage\"=\"undamaged\",\"direction\"=2]",
                 "2323": "minecraft:anvil [\"damage\"=\"undamaged\",\"direction\"=3]",
                 "2324": "minecraft:anvil [\"damage\"=\"slightly_damaged\",\"direction\"=0]",
                 "2325": "minecraft:anvil [\"damage\"=\"slightly_damaged\",\"direction\"=1]",
                 "2326": "minecraft:anvil [\"damage\"=\"slightly_damaged\",\"direction\"=2]",
                 "2327": "minecraft:anvil [\"damage\"=\"slightly_damaged\",\"direction\"=3]",
                 "2328": "minecraft:anvil [\"damage\"=\"very_damaged\",\"direction\"=0]",
                 "2329": "minecraft:anvil [\"damage\"=\"very_damaged\",\"direction\"=1]",
                 "2330": "minecraft:anvil [\"damage\"=\"very_damaged\",\"direction\"=2]",
                 "2331": "minecraft:anvil [\"damage\"=\"very_damaged\",\"direction\"=3]",
                 "2338": "minecraft:trapped_chest [\"facing_direction\"=2]",
                 "2339": "minecraft:trapped_chest [\"facing_direction\"=3]",
                 "2340": "minecraft:trapped_chest [\"facing_direction\"=4]",
                 "2341": "minecraft:trapped_chest [\"facing_direction\"=5]",
                 "2352": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=0]",
                 "2353": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=1]",
                 "2354": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=2]",
                 "2355": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=3]",
                 "2356": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=4]",
                 "2357": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=5]",
                 "2358": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=6]",
                 "2359": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=7]",
                 "2360": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=8]",
                 "2361": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=9]",
                 "2362": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=10]",
                 "2363": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=11]",
                 "2364": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=12]",
                 "2365": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=13]",
                 "2366": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=14]",
                 "2367": "minecraft:light_weighted_pressure_plate [\"redstone_signal\"=15]",
                 "2368": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=0]",
                 "2369": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=1]",
                 "2370": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=2]",
                 "2371": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=3]",
                 "2372": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=4]",
                 "2373": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=5]",
                 "2374": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=6]",
                 "2375": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=7]",
                 "2376": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=8]",
                 "2377": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=9]",
                 "2378": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=10]",
                 "2379": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=11]",
                 "2380": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=12]",
                 "2381": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=13]",
                 "2382": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=14]",
                 "2383": "minecraft:heavy_weighted_pressure_plate [\"redstone_signal\"=15]",
                 "2400": "minecraft:unpowered_comparator [\"output_subtract_bit\"=false,\"output_lit_bit\"=false,\"direction\"=0]",
                 "2401": "minecraft:unpowered_comparator [\"output_subtract_bit\"=false,\"output_lit_bit\"=false,\"direction\"=1]",
                 "2402": "minecraft:unpowered_comparator [\"output_subtract_bit\"=false,\"output_lit_bit\"=false,\"direction\"=2]",
                 "2403": "minecraft:unpowered_comparator [\"output_subtract_bit\"=false,\"output_lit_bit\"=false,\"direction\"=3]",
                 "2404": "minecraft:unpowered_comparator [\"output_subtract_bit\"=true,\"output_lit_bit\"=false,\"direction\"=0]",
                 "2405": "minecraft:unpowered_comparator [\"output_subtract_bit\"=true,\"output_lit_bit\"=false,\"direction\"=1]",
                 "2406": "minecraft:unpowered_comparator [\"output_subtract_bit\"=true,\"output_lit_bit\"=false,\"direction\"=2]",
                 "2407": "minecraft:unpowered_comparator [\"output_subtract_bit\"=true,\"output_lit_bit\"=false,\"direction\"=3]",
                 "2408": "minecraft:powered_comparator [\"output_subtract_bit\"=false,\"output_lit_bit\"=true,\"direction\"=0]",
                 "2409": "minecraft:powered_comparator [\"output_subtract_bit\"=false,\"output_lit_bit\"=true,\"direction\"=1]",
                 "2410": "minecraft:powered_comparator [\"output_subtract_bit\"=false,\"output_lit_bit\"=true,\"direction\"=2]",
                 "2411": "minecraft:powered_comparator [\"output_subtract_bit\"=false,\"output_lit_bit\"=true,\"direction\"=3]",
                 "2412": "minecraft:powered_comparator [\"output_subtract_bit\"=true,\"output_lit_bit\"=true,\"direction\"=0]",
                 "2413": "minecraft:powered_comparator [\"output_subtract_bit\"=true,\"output_lit_bit\"=true,\"direction\"=1]",
                 "2414": "minecraft:powered_comparator [\"output_subtract_bit\"=true,\"output_lit_bit\"=true,\"direction\"=2]",
                 "2415": "minecraft:powered_comparator [\"output_subtract_bit\"=true,\"output_lit_bit\"=true,\"direction\"=3]",
                 "2416": "minecraft:daylight_detector [\"redstone_signal\"=0]",
                 "2417": "minecraft:daylight_detector [\"redstone_signal\"=1]",
                 "2418": "minecraft:daylight_detector [\"redstone_signal\"=2]",
                 "2419": "minecraft:daylight_detector [\"redstone_signal\"=3]",
                 "2420": "minecraft:daylight_detector [\"redstone_signal\"=4]",
                 "2421": "minecraft:daylight_detector [\"redstone_signal\"=5]",
                 "2422": "minecraft:daylight_detector [\"redstone_signal\"=6]",
                 "2423": "minecraft:daylight_detector [\"redstone_signal\"=7]",
                 "2424": "minecraft:daylight_detector [\"redstone_signal\"=8]",
                 "2425": "minecraft:daylight_detector [\"redstone_signal\"=9]",
                 "2426": "minecraft:daylight_detector [\"redstone_signal\"=10]",
                 "2427": "minecraft:daylight_detector [\"redstone_signal\"=11]",
                 "2428": "minecraft:daylight_detector [\"redstone_signal\"=12]",
                 "2429": "minecraft:daylight_detector [\"redstone_signal\"=13]",
                 "2430": "minecraft:daylight_detector [\"redstone_signal\"=14]",
                 "2431": "minecraft:daylight_detector [\"redstone_signal\"=15]", "2432": "minecraft:redstone_block",
                 "2448": "minecraft:quartz_ore",
                 "2464": "minecraft:hopper [\"facing_direction\"=0,\"toggle_bit\"=true]",
                 "2466": "minecraft:hopper [\"facing_direction\"=2,\"toggle_bit\"=true]",
                 "2467": "minecraft:hopper [\"facing_direction\"=3,\"toggle_bit\"=true]",
                 "2468": "minecraft:hopper [\"facing_direction\"=4,\"toggle_bit\"=true]",
                 "2469": "minecraft:hopper [\"facing_direction\"=5,\"toggle_bit\"=true]",
                 "2472": "minecraft:hopper [\"facing_direction\"=0,\"toggle_bit\"=false]",
                 "2474": "minecraft:hopper [\"facing_direction\"=2,\"toggle_bit\"=false]",
                 "2475": "minecraft:hopper [\"facing_direction\"=3,\"toggle_bit\"=false]",
                 "2476": "minecraft:hopper [\"facing_direction\"=4,\"toggle_bit\"=false]",
                 "2477": "minecraft:hopper [\"facing_direction\"=5,\"toggle_bit\"=false]",
                 "2480": "minecraft:quartz_block [\"chisel_type\"=\"default\",\"pillar_axis\"=\"y\"]",
                 "2481": "minecraft:quartz_block [\"chisel_type\"=\"chiseled\",\"pillar_axis\"=\"y\"]",
                 "2482": "minecraft:quartz_block [\"chisel_type\"=\"lines\",\"pillar_axis\"=\"y\"]",
                 "2483": "minecraft:quartz_block [\"chisel_type\"=\"lines\",\"pillar_axis\"=\"x\"]",
                 "2484": "minecraft:quartz_block [\"chisel_type\"=\"lines\",\"pillar_axis\"=\"z\"]",
                 "2496": "minecraft:quartz_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "2497": "minecraft:quartz_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "2498": "minecraft:quartz_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "2499": "minecraft:quartz_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "2500": "minecraft:quartz_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "2501": "minecraft:quartz_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "2502": "minecraft:quartz_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "2503": "minecraft:quartz_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "2512": "minecraft:activator_rail [\"rail_data_bit\"=false,\"rail_direction\"=0]",
                 "2513": "minecraft:activator_rail [\"rail_data_bit\"=false,\"rail_direction\"=1]",
                 "2514": "minecraft:activator_rail [\"rail_data_bit\"=false,\"rail_direction\"=2]",
                 "2515": "minecraft:activator_rail [\"rail_data_bit\"=false,\"rail_direction\"=3]",
                 "2516": "minecraft:activator_rail [\"rail_data_bit\"=false,\"rail_direction\"=4]",
                 "2517": "minecraft:activator_rail [\"rail_data_bit\"=false,\"rail_direction\"=5]",
                 "2520": "minecraft:activator_rail [\"rail_data_bit\"=true,\"rail_direction\"=0]",
                 "2521": "minecraft:activator_rail [\"rail_data_bit\"=true,\"rail_direction\"=1]",
                 "2522": "minecraft:activator_rail [\"rail_data_bit\"=true,\"rail_direction\"=2]",
                 "2523": "minecraft:activator_rail [\"rail_data_bit\"=true,\"rail_direction\"=3]",
                 "2524": "minecraft:activator_rail [\"rail_data_bit\"=true,\"rail_direction\"=4]",
                 "2525": "minecraft:activator_rail [\"rail_data_bit\"=true,\"rail_direction\"=5]",
                 "2528": "minecraft:dropper [\"facing_direction\"=0,\"triggered_bit\"=false]",
                 "2529": "minecraft:dropper [\"facing_direction\"=1,\"triggered_bit\"=false]",
                 "2530": "minecraft:dropper [\"facing_direction\"=2,\"triggered_bit\"=false]",
                 "2531": "minecraft:dropper [\"facing_direction\"=3,\"triggered_bit\"=false]",
                 "2532": "minecraft:dropper [\"facing_direction\"=4,\"triggered_bit\"=false]",
                 "2533": "minecraft:dropper [\"facing_direction\"=5,\"triggered_bit\"=false]",
                 "2536": "minecraft:dropper [\"facing_direction\"=0,\"triggered_bit\"=true]",
                 "2537": "minecraft:dropper [\"facing_direction\"=1,\"triggered_bit\"=true]",
                 "2538": "minecraft:dropper [\"facing_direction\"=2,\"triggered_bit\"=true]",
                 "2539": "minecraft:dropper [\"facing_direction\"=3,\"triggered_bit\"=true]",
                 "2540": "minecraft:dropper [\"facing_direction\"=4,\"triggered_bit\"=true]",
                 "2541": "minecraft:dropper [\"facing_direction\"=5,\"triggered_bit\"=true]",
                 "2544": "minecraft:stained_hardened_clay [\"color\"=\"white\"]",
                 "2545": "minecraft:stained_hardened_clay [\"color\"=\"orange\"]",
                 "2546": "minecraft:stained_hardened_clay [\"color\"=\"magenta\"]",
                 "2547": "minecraft:stained_hardened_clay [\"color\"=\"light_blue\"]",
                 "2548": "minecraft:stained_hardened_clay [\"color\"=\"yellow\"]",
                 "2549": "minecraft:stained_hardened_clay [\"color\"=\"lime\"]",
                 "2550": "minecraft:stained_hardened_clay [\"color\"=\"pink\"]",
                 "2551": "minecraft:stained_hardened_clay [\"color\"=\"gray\"]",
                 "2552": "minecraft:stained_hardened_clay [\"color\"=\"silver\"]",
                 "2553": "minecraft:stained_hardened_clay [\"color\"=\"cyan\"]",
                 "2554": "minecraft:stained_hardened_clay [\"color\"=\"purple\"]",
                 "2555": "minecraft:stained_hardened_clay [\"color\"=\"blue\"]",
                 "2556": "minecraft:stained_hardened_clay [\"color\"=\"brown\"]",
                 "2557": "minecraft:stained_hardened_clay [\"color\"=\"green\"]",
                 "2558": "minecraft:stained_hardened_clay [\"color\"=\"red\"]",
                 "2559": "minecraft:stained_hardened_clay [\"color\"=\"black\"]",
                 "2560": "minecraft:stained_glass_pane [\"color\"=\"white\"]",
                 "2561": "minecraft:stained_glass_pane [\"color\"=\"orange\"]",
                 "2562": "minecraft:stained_glass_pane [\"color\"=\"magenta\"]",
                 "2563": "minecraft:stained_glass_pane [\"color\"=\"light_blue\"]",
                 "2564": "minecraft:stained_glass_pane [\"color\"=\"yellow\"]",
                 "2565": "minecraft:stained_glass_pane [\"color\"=\"lime\"]",
                 "2566": "minecraft:stained_glass_pane [\"color\"=\"pink\"]",
                 "2567": "minecraft:stained_glass_pane [\"color\"=\"gray\"]",
                 "2568": "minecraft:stained_glass_pane [\"color\"=\"silver\"]",
                 "2569": "minecraft:stained_glass_pane [\"color\"=\"cyan\"]",
                 "2570": "minecraft:stained_glass_pane [\"color\"=\"purple\"]",
                 "2571": "minecraft:stained_glass_pane [\"color\"=\"blue\"]",
                 "2572": "minecraft:stained_glass_pane [\"color\"=\"brown\"]",
                 "2573": "minecraft:stained_glass_pane [\"color\"=\"green\"]",
                 "2574": "minecraft:stained_glass_pane [\"color\"=\"red\"]",
                 "2575": "minecraft:stained_glass_pane [\"color\"=\"black\"]",
                 "2576": "minecraft:leaves2 [\"persistent_bit\"=false,\"update_bit\"=false,\"new_leaf_type\"=\"acacia\"]",
                 "2577": "minecraft:leaves2 [\"persistent_bit\"=false,\"update_bit\"=false,\"new_leaf_type\"=\"dark_oak\"]",
                 "2580": "minecraft:leaves2 [\"persistent_bit\"=true,\"update_bit\"=false,\"new_leaf_type\"=\"acacia\"]",
                 "2581": "minecraft:leaves2 [\"persistent_bit\"=true,\"update_bit\"=false,\"new_leaf_type\"=\"dark_oak\"]",
                 "2584": "minecraft:leaves2 [\"persistent_bit\"=false,\"update_bit\"=false,\"new_leaf_type\"=\"acacia\"]",
                 "2585": "minecraft:leaves2 [\"persistent_bit\"=false,\"update_bit\"=false,\"new_leaf_type\"=\"dark_oak\"]",
                 "2588": "minecraft:leaves2 [\"persistent_bit\"=true,\"update_bit\"=false,\"new_leaf_type\"=\"acacia\"]",
                 "2589": "minecraft:leaves2 [\"persistent_bit\"=true,\"update_bit\"=false,\"new_leaf_type\"=\"dark_oak\"]",
                 "2592": "minecraft:log2 [\"pillar_axis\"=\"y\",\"new_log_type\"=\"acacia\"]",
                 "2593": "minecraft:log2 [\"pillar_axis\"=\"y\",\"new_log_type\"=\"dark_oak\"]",
                 "2596": "minecraft:log2 [\"pillar_axis\"=\"x\",\"new_log_type\"=\"acacia\"]",
                 "2597": "minecraft:log2 [\"pillar_axis\"=\"x\",\"new_log_type\"=\"dark_oak\"]",
                 "2600": "minecraft:log2 [\"pillar_axis\"=\"z\",\"new_log_type\"=\"acacia\"]",
                 "2601": "minecraft:log2 [\"pillar_axis\"=\"z\",\"new_log_type\"=\"dark_oak\"]",
                 "2604": "minecraft:wood [\"stripped_bit\"=false,\"pillar_axis\"=\"y\",\"wood_type\"=\"acacia\"]",
                 "2605": "minecraft:wood [\"stripped_bit\"=false,\"pillar_axis\"=\"y\",\"wood_type\"=\"dark_oak\"]",
                 "2608": "minecraft:acacia_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "2609": "minecraft:acacia_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "2610": "minecraft:acacia_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "2611": "minecraft:acacia_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "2612": "minecraft:acacia_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "2613": "minecraft:acacia_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "2614": "minecraft:acacia_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "2615": "minecraft:acacia_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "2624": "minecraft:dark_oak_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "2625": "minecraft:dark_oak_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "2626": "minecraft:dark_oak_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "2627": "minecraft:dark_oak_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "2628": "minecraft:dark_oak_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "2629": "minecraft:dark_oak_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "2630": "minecraft:dark_oak_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "2631": "minecraft:dark_oak_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "2640": "minecraft:slime", "2656": "minecraft:barrier",
                 "2672": "minecraft:iron_trapdoor [\"open_bit\"=false,\"upside_down_bit\"=false,\"direction\"=3]",
                 "2673": "minecraft:iron_trapdoor [\"open_bit\"=false,\"upside_down_bit\"=false,\"direction\"=2]",
                 "2674": "minecraft:iron_trapdoor [\"open_bit\"=false,\"upside_down_bit\"=false,\"direction\"=1]",
                 "2675": "minecraft:iron_trapdoor [\"open_bit\"=false,\"upside_down_bit\"=false,\"direction\"=0]",
                 "2676": "minecraft:iron_trapdoor [\"open_bit\"=true,\"upside_down_bit\"=false,\"direction\"=3]",
                 "2677": "minecraft:iron_trapdoor [\"open_bit\"=true,\"upside_down_bit\"=false,\"direction\"=2]",
                 "2678": "minecraft:iron_trapdoor [\"open_bit\"=true,\"upside_down_bit\"=false,\"direction\"=1]",
                 "2679": "minecraft:iron_trapdoor [\"open_bit\"=true,\"upside_down_bit\"=false,\"direction\"=0]",
                 "2680": "minecraft:iron_trapdoor [\"open_bit\"=false,\"upside_down_bit\"=true,\"direction\"=3]",
                 "2681": "minecraft:iron_trapdoor [\"open_bit\"=false,\"upside_down_bit\"=true,\"direction\"=2]",
                 "2682": "minecraft:iron_trapdoor [\"open_bit\"=false,\"upside_down_bit\"=true,\"direction\"=1]",
                 "2683": "minecraft:iron_trapdoor [\"open_bit\"=false,\"upside_down_bit\"=true,\"direction\"=0]",
                 "2684": "minecraft:iron_trapdoor [\"open_bit\"=true,\"upside_down_bit\"=true,\"direction\"=3]",
                 "2685": "minecraft:iron_trapdoor [\"open_bit\"=true,\"upside_down_bit\"=true,\"direction\"=2]",
                 "2686": "minecraft:iron_trapdoor [\"open_bit\"=true,\"upside_down_bit\"=true,\"direction\"=1]",
                 "2687": "minecraft:iron_trapdoor [\"open_bit\"=true,\"upside_down_bit\"=true,\"direction\"=0]",
                 "2688": "minecraft:prismarine [\"prismarine_block_type\"=\"default\"]",
                 "2689": "minecraft:prismarine [\"prismarine_block_type\"=\"bricks\"]",
                 "2690": "minecraft:prismarine [\"prismarine_block_type\"=\"dark\"]", "2704": "minecraft:sea_lantern",
                 "2720": "minecraft:hay_block [\"pillar_axis\"=\"y\",\"deprecated\"=0]",
                 "2724": "minecraft:hay_block [\"pillar_axis\"=\"x\",\"deprecated\"=0]",
                 "2728": "minecraft:hay_block [\"pillar_axis\"=\"z\",\"deprecated\"=0]",
                 "2736": "minecraft:carpet [\"color\"=\"white\"]", "2737": "minecraft:carpet [\"color\"=\"orange\"]",
                 "2738": "minecraft:carpet [\"color\"=\"magenta\"]",
                 "2739": "minecraft:carpet [\"color\"=\"light_blue\"]",
                 "2740": "minecraft:carpet [\"color\"=\"yellow\"]", "2741": "minecraft:carpet [\"color\"=\"lime\"]",
                 "2742": "minecraft:carpet [\"color\"=\"pink\"]", "2743": "minecraft:carpet [\"color\"=\"gray\"]",
                 "2744": "minecraft:carpet [\"color\"=\"silver\"]", "2745": "minecraft:carpet [\"color\"=\"cyan\"]",
                 "2746": "minecraft:carpet [\"color\"=\"purple\"]", "2747": "minecraft:carpet [\"color\"=\"blue\"]",
                 "2748": "minecraft:carpet [\"color\"=\"brown\"]", "2749": "minecraft:carpet [\"color\"=\"green\"]",
                 "2750": "minecraft:carpet [\"color\"=\"red\"]", "2751": "minecraft:carpet [\"color\"=\"black\"]",
                 "2752": "minecraft:hardened_clay", "2768": "minecraft:coal_block", "2784": "minecraft:packed_ice",
                 "2800": "minecraft:double_plant [\"upper_block_bit\"=false,\"double_plant_type\"=\"sunflower\"]",
                 "2801": "minecraft:double_plant [\"upper_block_bit\"=false,\"double_plant_type\"=\"syringa\"]",
                 "2802": "minecraft:double_plant [\"upper_block_bit\"=false,\"double_plant_type\"=\"grass\"]",
                 "2803": "minecraft:double_plant [\"upper_block_bit\"=false,\"double_plant_type\"=\"fern\"]",
                 "2804": "minecraft:double_plant [\"upper_block_bit\"=false,\"double_plant_type\"=\"rose\"]",
                 "2805": "minecraft:double_plant [\"upper_block_bit\"=false,\"double_plant_type\"=\"paeonia\"]",
                 "2811": "minecraft:double_plant [\"upper_block_bit\"=true,\"double_plant_type\"=\"paeonia\"]",
                 "2816": "minecraft:standing_banner [\"ground_sign_direction\"=0]",
                 "2817": "minecraft:standing_banner [\"ground_sign_direction\"=1]",
                 "2818": "minecraft:standing_banner [\"ground_sign_direction\"=2]",
                 "2819": "minecraft:standing_banner [\"ground_sign_direction\"=3]",
                 "2820": "minecraft:standing_banner [\"ground_sign_direction\"=4]",
                 "2821": "minecraft:standing_banner [\"ground_sign_direction\"=5]",
                 "2822": "minecraft:standing_banner [\"ground_sign_direction\"=6]",
                 "2823": "minecraft:standing_banner [\"ground_sign_direction\"=7]",
                 "2824": "minecraft:standing_banner [\"ground_sign_direction\"=8]",
                 "2825": "minecraft:standing_banner [\"ground_sign_direction\"=9]",
                 "2826": "minecraft:standing_banner [\"ground_sign_direction\"=10]",
                 "2827": "minecraft:standing_banner [\"ground_sign_direction\"=11]",
                 "2828": "minecraft:standing_banner [\"ground_sign_direction\"=12]",
                 "2829": "minecraft:standing_banner [\"ground_sign_direction\"=13]",
                 "2830": "minecraft:standing_banner [\"ground_sign_direction\"=14]",
                 "2831": "minecraft:standing_banner [\"ground_sign_direction\"=15]",
                 "2834": "minecraft:wall_banner [\"facing_direction\"=2]",
                 "2835": "minecraft:wall_banner [\"facing_direction\"=3]",
                 "2836": "minecraft:wall_banner [\"facing_direction\"=4]",
                 "2837": "minecraft:wall_banner [\"facing_direction\"=5]",
                 "2848": "minecraft:daylight_detector_inverted [\"redstone_signal\"=0]",
                 "2849": "minecraft:daylight_detector_inverted [\"redstone_signal\"=1]",
                 "2850": "minecraft:daylight_detector_inverted [\"redstone_signal\"=2]",
                 "2851": "minecraft:daylight_detector_inverted [\"redstone_signal\"=3]",
                 "2852": "minecraft:daylight_detector_inverted [\"redstone_signal\"=4]",
                 "2853": "minecraft:daylight_detector_inverted [\"redstone_signal\"=5]",
                 "2854": "minecraft:daylight_detector_inverted [\"redstone_signal\"=6]",
                 "2855": "minecraft:daylight_detector_inverted [\"redstone_signal\"=7]",
                 "2856": "minecraft:daylight_detector_inverted [\"redstone_signal\"=8]",
                 "2857": "minecraft:daylight_detector_inverted [\"redstone_signal\"=9]",
                 "2858": "minecraft:daylight_detector_inverted [\"redstone_signal\"=10]",
                 "2859": "minecraft:daylight_detector_inverted [\"redstone_signal\"=11]",
                 "2860": "minecraft:daylight_detector_inverted [\"redstone_signal\"=12]",
                 "2861": "minecraft:daylight_detector_inverted [\"redstone_signal\"=13]",
                 "2862": "minecraft:daylight_detector_inverted [\"redstone_signal\"=14]",
                 "2863": "minecraft:daylight_detector_inverted [\"redstone_signal\"=15]",
                 "2864": "minecraft:red_sandstone [\"sand_stone_type\"=\"default\"]",
                 "2865": "minecraft:red_sandstone [\"sand_stone_type\"=\"heiroglyphs\"]",
                 "2866": "minecraft:red_sandstone [\"sand_stone_type\"=\"cut\"]",
                 "2880": "minecraft:red_sandstone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "2881": "minecraft:red_sandstone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "2882": "minecraft:red_sandstone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "2883": "minecraft:red_sandstone_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "2884": "minecraft:red_sandstone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "2885": "minecraft:red_sandstone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "2886": "minecraft:red_sandstone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "2887": "minecraft:red_sandstone_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "2896": "minecraft:double_stone_block_slab2 [\"stone_slab_type_2\"=\"red_sandstone\",\"top_slot_bit\"=false]",
                 "2904": "minecraft:red_sandstone [\"sand_stone_type\"=\"smooth\"]",
                 "2912": "minecraft:stone_block_slab2 [\"stone_slab_type_2\"=\"red_sandstone\",\"top_slot_bit\"=false]",
                 "2920": "minecraft:stone_block_slab2 [\"stone_slab_type_2\"=\"red_sandstone\",\"top_slot_bit\"=true]",
                 "2928": "minecraft:spruce_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2929": "minecraft:spruce_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2930": "minecraft:spruce_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2931": "minecraft:spruce_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2932": "minecraft:spruce_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2933": "minecraft:spruce_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2934": "minecraft:spruce_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2935": "minecraft:spruce_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2936": "minecraft:spruce_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2937": "minecraft:spruce_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2938": "minecraft:spruce_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2939": "minecraft:spruce_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2940": "minecraft:spruce_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2941": "minecraft:spruce_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2942": "minecraft:spruce_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2943": "minecraft:spruce_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2944": "minecraft:birch_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2945": "minecraft:birch_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2946": "minecraft:birch_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2947": "minecraft:birch_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2948": "minecraft:birch_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2949": "minecraft:birch_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2950": "minecraft:birch_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2951": "minecraft:birch_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2952": "minecraft:birch_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2953": "minecraft:birch_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2954": "minecraft:birch_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2955": "minecraft:birch_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2956": "minecraft:birch_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2957": "minecraft:birch_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2958": "minecraft:birch_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2959": "minecraft:birch_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2960": "minecraft:jungle_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2961": "minecraft:jungle_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2962": "minecraft:jungle_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2963": "minecraft:jungle_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2964": "minecraft:jungle_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2965": "minecraft:jungle_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2966": "minecraft:jungle_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2967": "minecraft:jungle_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2968": "minecraft:jungle_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2969": "minecraft:jungle_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2970": "minecraft:jungle_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2971": "minecraft:jungle_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2972": "minecraft:jungle_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2973": "minecraft:jungle_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2974": "minecraft:jungle_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2975": "minecraft:jungle_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2976": "minecraft:dark_oak_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2977": "minecraft:dark_oak_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2978": "minecraft:dark_oak_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2979": "minecraft:dark_oak_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2980": "minecraft:dark_oak_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2981": "minecraft:dark_oak_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2982": "minecraft:dark_oak_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2983": "minecraft:dark_oak_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2984": "minecraft:dark_oak_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2985": "minecraft:dark_oak_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2986": "minecraft:dark_oak_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2987": "minecraft:dark_oak_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2988": "minecraft:dark_oak_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2989": "minecraft:dark_oak_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2990": "minecraft:dark_oak_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2991": "minecraft:dark_oak_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2992": "minecraft:acacia_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2993": "minecraft:acacia_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2994": "minecraft:acacia_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2995": "minecraft:acacia_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "2996": "minecraft:acacia_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "2997": "minecraft:acacia_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "2998": "minecraft:acacia_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "2999": "minecraft:acacia_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "3000": "minecraft:acacia_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=0]",
                 "3001": "minecraft:acacia_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=1]",
                 "3002": "minecraft:acacia_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=2]",
                 "3003": "minecraft:acacia_fence_gate [\"open_bit\"=false,\"in_wall_bit\"=false,\"direction\"=3]",
                 "3004": "minecraft:acacia_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=0]",
                 "3005": "minecraft:acacia_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=1]",
                 "3006": "minecraft:acacia_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=2]",
                 "3007": "minecraft:acacia_fence_gate [\"open_bit\"=true,\"in_wall_bit\"=false,\"direction\"=3]",
                 "3008": "minecraft:fence [\"wood_type\"=\"spruce\"]",
                 "3024": "minecraft:fence [\"wood_type\"=\"birch\"]",
                 "3040": "minecraft:fence [\"wood_type\"=\"jungle\"]",
                 "3056": "minecraft:fence [\"wood_type\"=\"dark_oak\"]",
                 "3072": "minecraft:fence [\"wood_type\"=\"acacia\"]",
                 "3088": "minecraft:spruce_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3089": "minecraft:spruce_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3090": "minecraft:spruce_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3091": "minecraft:spruce_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3092": "minecraft:spruce_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3093": "minecraft:spruce_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3094": "minecraft:spruce_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3095": "minecraft:spruce_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3096": "minecraft:spruce_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3097": "minecraft:spruce_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3098": "minecraft:spruce_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3099": "minecraft:spruce_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3104": "minecraft:birch_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3105": "minecraft:birch_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3106": "minecraft:birch_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3107": "minecraft:birch_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3108": "minecraft:birch_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3109": "minecraft:birch_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3110": "minecraft:birch_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3111": "minecraft:birch_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3112": "minecraft:birch_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3113": "minecraft:birch_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3114": "minecraft:birch_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3115": "minecraft:birch_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3120": "minecraft:jungle_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3121": "minecraft:jungle_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3122": "minecraft:jungle_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3123": "minecraft:jungle_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3124": "minecraft:jungle_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3125": "minecraft:jungle_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3126": "minecraft:jungle_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3127": "minecraft:jungle_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3128": "minecraft:jungle_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3129": "minecraft:jungle_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3130": "minecraft:jungle_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3131": "minecraft:jungle_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3136": "minecraft:acacia_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3137": "minecraft:acacia_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3138": "minecraft:acacia_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3139": "minecraft:acacia_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3140": "minecraft:acacia_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3141": "minecraft:acacia_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3142": "minecraft:acacia_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3143": "minecraft:acacia_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3144": "minecraft:acacia_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3145": "minecraft:acacia_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3146": "minecraft:acacia_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3147": "minecraft:acacia_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3152": "minecraft:dark_oak_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3153": "minecraft:dark_oak_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3154": "minecraft:dark_oak_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3155": "minecraft:dark_oak_door [\"open_bit\"=false,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3156": "minecraft:dark_oak_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3157": "minecraft:dark_oak_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=1]",
                 "3158": "minecraft:dark_oak_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=2]",
                 "3159": "minecraft:dark_oak_door [\"open_bit\"=true,\"upper_block_bit\"=false,\"door_hinge_bit\"=true,\"direction\"=3]",
                 "3160": "minecraft:dark_oak_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3161": "minecraft:dark_oak_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3162": "minecraft:dark_oak_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=false,\"direction\"=0]",
                 "3163": "minecraft:dark_oak_door [\"open_bit\"=false,\"upper_block_bit\"=true,\"door_hinge_bit\"=true,\"direction\"=0]",
                 "3168": "minecraft:end_rod [\"facing_direction\"=0]",
                 "3169": "minecraft:end_rod [\"facing_direction\"=1]",
                 "3170": "minecraft:end_rod [\"facing_direction\"=3]",
                 "3171": "minecraft:end_rod [\"facing_direction\"=2]",
                 "3172": "minecraft:end_rod [\"facing_direction\"=5]",
                 "3173": "minecraft:end_rod [\"facing_direction\"=4]", "3184": "minecraft:chorus_plant",
                 "3200": "minecraft:chorus_flower [\"age\"=0]", "3201": "minecraft:chorus_flower [\"age\"=1]",
                 "3202": "minecraft:chorus_flower [\"age\"=2]", "3203": "minecraft:chorus_flower [\"age\"=3]",
                 "3204": "minecraft:chorus_flower [\"age\"=4]", "3205": "minecraft:chorus_flower [\"age\"=5]",
                 "3216": "minecraft:purpur_block [\"chisel_type\"=\"default\",\"pillar_axis\"=\"y\"]",
                 "3232": "minecraft:purpur_block [\"chisel_type\"=\"lines\",\"pillar_axis\"=\"y\"]",
                 "3236": "minecraft:purpur_block [\"chisel_type\"=\"lines\",\"pillar_axis\"=\"x\"]",
                 "3240": "minecraft:purpur_block [\"chisel_type\"=\"lines\",\"pillar_axis\"=\"z\"]",
                 "3248": "minecraft:purpur_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=0]",
                 "3249": "minecraft:purpur_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=1]",
                 "3250": "minecraft:purpur_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=2]",
                 "3251": "minecraft:purpur_stairs [\"upside_down_bit\"=false,\"weirdo_direction\"=3]",
                 "3252": "minecraft:purpur_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=0]",
                 "3253": "minecraft:purpur_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=1]",
                 "3254": "minecraft:purpur_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=2]",
                 "3255": "minecraft:purpur_stairs [\"upside_down_bit\"=true,\"weirdo_direction\"=3]",
                 "3264": "minecraft:double_stone_block_slab2 [\"stone_slab_type_2\"=\"purpur\",\"top_slot_bit\"=false]",
                 "3280": "minecraft:stone_block_slab2 [\"stone_slab_type_2\"=\"purpur\",\"top_slot_bit\"=false]",
                 "3288": "minecraft:stone_block_slab2 [\"stone_slab_type_2\"=\"purpur\",\"top_slot_bit\"=true]",
                 "3296": "minecraft:end_bricks", "3312": "minecraft:beetroot [\"growth\"=0]",
                 "3313": "minecraft:beetroot [\"growth\"=3]", "3314": "minecraft:beetroot [\"growth\"=4]",
                 "3315": "minecraft:beetroot [\"growth\"=7]", "3328": "minecraft:grass_path",
                 "3344": "minecraft:end_gateway",
                 "3360": "minecraft:repeating_command_block [\"conditional_bit\"=false,\"facing_direction\"=0]",
                 "3361": "minecraft:repeating_command_block [\"conditional_bit\"=false,\"facing_direction\"=1]",
                 "3362": "minecraft:repeating_command_block [\"conditional_bit\"=false,\"facing_direction\"=2]",
                 "3363": "minecraft:repeating_command_block [\"conditional_bit\"=false,\"facing_direction\"=3]",
                 "3364": "minecraft:repeating_command_block [\"conditional_bit\"=false,\"facing_direction\"=4]",
                 "3365": "minecraft:repeating_command_block [\"conditional_bit\"=false,\"facing_direction\"=5]",
                 "3368": "minecraft:repeating_command_block [\"conditional_bit\"=true,\"facing_direction\"=0]",
                 "3369": "minecraft:repeating_command_block [\"conditional_bit\"=true,\"facing_direction\"=1]",
                 "3370": "minecraft:repeating_command_block [\"conditional_bit\"=true,\"facing_direction\"=2]",
                 "3371": "minecraft:repeating_command_block [\"conditional_bit\"=true,\"facing_direction\"=3]",
                 "3372": "minecraft:repeating_command_block [\"conditional_bit\"=true,\"facing_direction\"=4]",
                 "3373": "minecraft:repeating_command_block [\"conditional_bit\"=true,\"facing_direction\"=5]",
                 "3376": "minecraft:chain_command_block [\"conditional_bit\"=false,\"facing_direction\"=0]",
                 "3377": "minecraft:chain_command_block [\"conditional_bit\"=false,\"facing_direction\"=1]",
                 "3378": "minecraft:chain_command_block [\"conditional_bit\"=false,\"facing_direction\"=2]",
                 "3379": "minecraft:chain_command_block [\"conditional_bit\"=false,\"facing_direction\"=3]",
                 "3380": "minecraft:chain_command_block [\"conditional_bit\"=false,\"facing_direction\"=4]",
                 "3381": "minecraft:chain_command_block [\"conditional_bit\"=false,\"facing_direction\"=5]",
                 "3384": "minecraft:chain_command_block [\"conditional_bit\"=true,\"facing_direction\"=0]",
                 "3385": "minecraft:chain_command_block [\"conditional_bit\"=true,\"facing_direction\"=1]",
                 "3386": "minecraft:chain_command_block [\"conditional_bit\"=true,\"facing_direction\"=2]",
                 "3387": "minecraft:chain_command_block [\"conditional_bit\"=true,\"facing_direction\"=3]",
                 "3388": "minecraft:chain_command_block [\"conditional_bit\"=true,\"facing_direction\"=4]",
                 "3389": "minecraft:chain_command_block [\"conditional_bit\"=true,\"facing_direction\"=5]",
                 "3392": "minecraft:frosted_ice [\"age\"=0]", "3393": "minecraft:frosted_ice [\"age\"=1]",
                 "3394": "minecraft:frosted_ice [\"age\"=2]", "3395": "minecraft:frosted_ice [\"age\"=3]",
                 "3408": "minecraft:magma", "3424": "minecraft:nether_wart_block", "3440": "minecraft:red_nether_brick",
                 "3456": "minecraft:bone_block [\"pillar_axis\"=\"y\",\"deprecated\"=0]",
                 "3460": "minecraft:bone_block [\"pillar_axis\"=\"x\",\"deprecated\"=0]",
                 "3464": "minecraft:bone_block [\"pillar_axis\"=\"z\",\"deprecated\"=0]",
                 "3472": "minecraft:structure_void [\"structure_void_type\"=\"air\"]",
                 "3488": "minecraft:observer [\"facing_direction\"=0,\"powered_bit\"=false]",
                 "3489": "minecraft:observer [\"facing_direction\"=1,\"powered_bit\"=false]",
                 "3490": "minecraft:observer [\"facing_direction\"=2,\"powered_bit\"=false]",
                 "3491": "minecraft:observer [\"facing_direction\"=3,\"powered_bit\"=false]",
                 "3492": "minecraft:observer [\"facing_direction\"=4,\"powered_bit\"=false]",
                 "3493": "minecraft:observer [\"facing_direction\"=5,\"powered_bit\"=false]",
                 "3496": "minecraft:observer [\"facing_direction\"=0,\"powered_bit\"=true]",
                 "3497": "minecraft:observer [\"facing_direction\"=1,\"powered_bit\"=true]",
                 "3498": "minecraft:observer [\"facing_direction\"=2,\"powered_bit\"=true]",
                 "3499": "minecraft:observer [\"facing_direction\"=3,\"powered_bit\"=true]",
                 "3500": "minecraft:observer [\"facing_direction\"=4,\"powered_bit\"=true]",
                 "3501": "minecraft:observer [\"facing_direction\"=5,\"powered_bit\"=true]",
                 "3504": "minecraft:shulker_box [\"color\"=\"white\"]",
                 "3505": "minecraft:shulker_box [\"color\"=\"white\"]",
                 "3506": "minecraft:shulker_box [\"color\"=\"white\"]",
                 "3507": "minecraft:shulker_box [\"color\"=\"white\"]",
                 "3508": "minecraft:shulker_box [\"color\"=\"white\"]",
                 "3509": "minecraft:shulker_box [\"color\"=\"white\"]",
                 "3520": "minecraft:shulker_box [\"color\"=\"orange\"]",
                 "3521": "minecraft:shulker_box [\"color\"=\"orange\"]",
                 "3522": "minecraft:shulker_box [\"color\"=\"orange\"]",
                 "3523": "minecraft:shulker_box [\"color\"=\"orange\"]",
                 "3524": "minecraft:shulker_box [\"color\"=\"orange\"]",
                 "3525": "minecraft:shulker_box [\"color\"=\"orange\"]",
                 "3536": "minecraft:shulker_box [\"color\"=\"magenta\"]",
                 "3537": "minecraft:shulker_box [\"color\"=\"magenta\"]",
                 "3538": "minecraft:shulker_box [\"color\"=\"magenta\"]",
                 "3539": "minecraft:shulker_box [\"color\"=\"magenta\"]",
                 "3540": "minecraft:shulker_box [\"color\"=\"magenta\"]",
                 "3541": "minecraft:shulker_box [\"color\"=\"magenta\"]",
                 "3552": "minecraft:shulker_box [\"color\"=\"light_blue\"]",
                 "3553": "minecraft:shulker_box [\"color\"=\"light_blue\"]",
                 "3554": "minecraft:shulker_box [\"color\"=\"light_blue\"]",
                 "3555": "minecraft:shulker_box [\"color\"=\"light_blue\"]",
                 "3556": "minecraft:shulker_box [\"color\"=\"light_blue\"]",
                 "3557": "minecraft:shulker_box [\"color\"=\"light_blue\"]",
                 "3568": "minecraft:shulker_box [\"color\"=\"yellow\"]",
                 "3569": "minecraft:shulker_box [\"color\"=\"yellow\"]",
                 "3570": "minecraft:shulker_box [\"color\"=\"yellow\"]",
                 "3571": "minecraft:shulker_box [\"color\"=\"yellow\"]",
                 "3572": "minecraft:shulker_box [\"color\"=\"yellow\"]",
                 "3573": "minecraft:shulker_box [\"color\"=\"yellow\"]",
                 "3584": "minecraft:shulker_box [\"color\"=\"lime\"]",
                 "3585": "minecraft:shulker_box [\"color\"=\"lime\"]",
                 "3586": "minecraft:shulker_box [\"color\"=\"lime\"]",
                 "3587": "minecraft:shulker_box [\"color\"=\"lime\"]",
                 "3588": "minecraft:shulker_box [\"color\"=\"lime\"]",
                 "3589": "minecraft:shulker_box [\"color\"=\"lime\"]",
                 "3600": "minecraft:shulker_box [\"color\"=\"pink\"]",
                 "3601": "minecraft:shulker_box [\"color\"=\"pink\"]",
                 "3602": "minecraft:shulker_box [\"color\"=\"pink\"]",
                 "3603": "minecraft:shulker_box [\"color\"=\"pink\"]",
                 "3604": "minecraft:shulker_box [\"color\"=\"pink\"]",
                 "3605": "minecraft:shulker_box [\"color\"=\"pink\"]",
                 "3616": "minecraft:shulker_box [\"color\"=\"gray\"]",
                 "3617": "minecraft:shulker_box [\"color\"=\"gray\"]",
                 "3618": "minecraft:shulker_box [\"color\"=\"gray\"]",
                 "3619": "minecraft:shulker_box [\"color\"=\"gray\"]",
                 "3620": "minecraft:shulker_box [\"color\"=\"gray\"]",
                 "3621": "minecraft:shulker_box [\"color\"=\"gray\"]",
                 "3632": "minecraft:shulker_box [\"color\"=\"silver\"]",
                 "3633": "minecraft:shulker_box [\"color\"=\"silver\"]",
                 "3634": "minecraft:shulker_box [\"color\"=\"silver\"]",
                 "3635": "minecraft:shulker_box [\"color\"=\"silver\"]",
                 "3636": "minecraft:shulker_box [\"color\"=\"silver\"]",
                 "3637": "minecraft:shulker_box [\"color\"=\"silver\"]",
                 "3648": "minecraft:shulker_box [\"color\"=\"cyan\"]",
                 "3649": "minecraft:shulker_box [\"color\"=\"cyan\"]",
                 "3650": "minecraft:shulker_box [\"color\"=\"cyan\"]",
                 "3651": "minecraft:shulker_box [\"color\"=\"cyan\"]",
                 "3652": "minecraft:shulker_box [\"color\"=\"cyan\"]",
                 "3653": "minecraft:shulker_box [\"color\"=\"cyan\"]",
                 "3664": "minecraft:shulker_box [\"color\"=\"purple\"]",
                 "3665": "minecraft:shulker_box [\"color\"=\"purple\"]",
                 "3666": "minecraft:shulker_box [\"color\"=\"purple\"]",
                 "3667": "minecraft:shulker_box [\"color\"=\"purple\"]",
                 "3668": "minecraft:shulker_box [\"color\"=\"purple\"]",
                 "3669": "minecraft:shulker_box [\"color\"=\"purple\"]",
                 "3680": "minecraft:shulker_box [\"color\"=\"blue\"]",
                 "3681": "minecraft:shulker_box [\"color\"=\"blue\"]",
                 "3682": "minecraft:shulker_box [\"color\"=\"blue\"]",
                 "3683": "minecraft:shulker_box [\"color\"=\"blue\"]",
                 "3684": "minecraft:shulker_box [\"color\"=\"blue\"]",
                 "3685": "minecraft:shulker_box [\"color\"=\"blue\"]",
                 "3696": "minecraft:shulker_box [\"color\"=\"brown\"]",
                 "3697": "minecraft:shulker_box [\"color\"=\"brown\"]",
                 "3698": "minecraft:shulker_box [\"color\"=\"brown\"]",
                 "3699": "minecraft:shulker_box [\"color\"=\"brown\"]",
                 "3700": "minecraft:shulker_box [\"color\"=\"brown\"]",
                 "3701": "minecraft:shulker_box [\"color\"=\"brown\"]",
                 "3712": "minecraft:shulker_box [\"color\"=\"green\"]",
                 "3713": "minecraft:shulker_box [\"color\"=\"green\"]",
                 "3714": "minecraft:shulker_box [\"color\"=\"green\"]",
                 "3715": "minecraft:shulker_box [\"color\"=\"green\"]",
                 "3716": "minecraft:shulker_box [\"color\"=\"green\"]",
                 "3717": "minecraft:shulker_box [\"color\"=\"green\"]",
                 "3728": "minecraft:shulker_box [\"color\"=\"red\"]",
                 "3729": "minecraft:shulker_box [\"color\"=\"red\"]",
                 "3730": "minecraft:shulker_box [\"color\"=\"red\"]",
                 "3731": "minecraft:shulker_box [\"color\"=\"red\"]",
                 "3732": "minecraft:shulker_box [\"color\"=\"red\"]",
                 "3733": "minecraft:shulker_box [\"color\"=\"red\"]",
                 "3744": "minecraft:shulker_box [\"color\"=\"black\"]",
                 "3745": "minecraft:shulker_box [\"color\"=\"black\"]",
                 "3746": "minecraft:shulker_box [\"color\"=\"black\"]",
                 "3747": "minecraft:shulker_box [\"color\"=\"black\"]",
                 "3748": "minecraft:shulker_box [\"color\"=\"black\"]",
                 "3749": "minecraft:shulker_box [\"color\"=\"black\"]",
                 "3760": "minecraft:white_glazed_terracotta [\"facing_direction\"=3]",
                 "3761": "minecraft:white_glazed_terracotta [\"facing_direction\"=4]",
                 "3762": "minecraft:white_glazed_terracotta [\"facing_direction\"=2]",
                 "3763": "minecraft:white_glazed_terracotta [\"facing_direction\"=5]",
                 "3776": "minecraft:orange_glazed_terracotta [\"facing_direction\"=3]",
                 "3777": "minecraft:orange_glazed_terracotta [\"facing_direction\"=4]",
                 "3778": "minecraft:orange_glazed_terracotta [\"facing_direction\"=2]",
                 "3779": "minecraft:orange_glazed_terracotta [\"facing_direction\"=5]",
                 "3792": "minecraft:magenta_glazed_terracotta [\"facing_direction\"=3]",
                 "3793": "minecraft:magenta_glazed_terracotta [\"facing_direction\"=4]",
                 "3794": "minecraft:magenta_glazed_terracotta [\"facing_direction\"=2]",
                 "3795": "minecraft:magenta_glazed_terracotta [\"facing_direction\"=5]",
                 "3808": "minecraft:light_blue_glazed_terracotta [\"facing_direction\"=3]",
                 "3809": "minecraft:light_blue_glazed_terracotta [\"facing_direction\"=4]",
                 "3810": "minecraft:light_blue_glazed_terracotta [\"facing_direction\"=2]",
                 "3811": "minecraft:light_blue_glazed_terracotta [\"facing_direction\"=5]",
                 "3824": "minecraft:yellow_glazed_terracotta [\"facing_direction\"=3]",
                 "3825": "minecraft:yellow_glazed_terracotta [\"facing_direction\"=4]",
                 "3826": "minecraft:yellow_glazed_terracotta [\"facing_direction\"=2]",
                 "3827": "minecraft:yellow_glazed_terracotta [\"facing_direction\"=5]",
                 "3840": "minecraft:lime_glazed_terracotta [\"facing_direction\"=3]",
                 "3841": "minecraft:lime_glazed_terracotta [\"facing_direction\"=4]",
                 "3842": "minecraft:lime_glazed_terracotta [\"facing_direction\"=2]",
                 "3843": "minecraft:lime_glazed_terracotta [\"facing_direction\"=5]",
                 "3856": "minecraft:pink_glazed_terracotta [\"facing_direction\"=3]",
                 "3857": "minecraft:pink_glazed_terracotta [\"facing_direction\"=4]",
                 "3858": "minecraft:pink_glazed_terracotta [\"facing_direction\"=2]",
                 "3859": "minecraft:pink_glazed_terracotta [\"facing_direction\"=5]",
                 "3872": "minecraft:gray_glazed_terracotta [\"facing_direction\"=3]",
                 "3873": "minecraft:gray_glazed_terracotta [\"facing_direction\"=4]",
                 "3874": "minecraft:gray_glazed_terracotta [\"facing_direction\"=2]",
                 "3875": "minecraft:gray_glazed_terracotta [\"facing_direction\"=5]",
                 "3888": "minecraft:silver_glazed_terracotta [\"facing_direction\"=3]",
                 "3889": "minecraft:silver_glazed_terracotta [\"facing_direction\"=4]",
                 "3890": "minecraft:silver_glazed_terracotta [\"facing_direction\"=2]",
                 "3891": "minecraft:silver_glazed_terracotta [\"facing_direction\"=5]",
                 "3904": "minecraft:cyan_glazed_terracotta [\"facing_direction\"=3]",
                 "3905": "minecraft:cyan_glazed_terracotta [\"facing_direction\"=4]",
                 "3906": "minecraft:cyan_glazed_terracotta [\"facing_direction\"=2]",
                 "3907": "minecraft:cyan_glazed_terracotta [\"facing_direction\"=5]",
                 "3920": "minecraft:purple_glazed_terracotta [\"facing_direction\"=3]",
                 "3921": "minecraft:purple_glazed_terracotta [\"facing_direction\"=4]",
                 "3922": "minecraft:purple_glazed_terracotta [\"facing_direction\"=2]",
                 "3923": "minecraft:purple_glazed_terracotta [\"facing_direction\"=5]",
                 "3936": "minecraft:blue_glazed_terracotta [\"facing_direction\"=3]",
                 "3937": "minecraft:blue_glazed_terracotta [\"facing_direction\"=4]",
                 "3938": "minecraft:blue_glazed_terracotta [\"facing_direction\"=2]",
                 "3939": "minecraft:blue_glazed_terracotta [\"facing_direction\"=5]",
                 "3952": "minecraft:brown_glazed_terracotta [\"facing_direction\"=3]",
                 "3953": "minecraft:brown_glazed_terracotta [\"facing_direction\"=4]",
                 "3954": "minecraft:brown_glazed_terracotta [\"facing_direction\"=2]",
                 "3955": "minecraft:brown_glazed_terracotta [\"facing_direction\"=5]",
                 "3968": "minecraft:green_glazed_terracotta [\"facing_direction\"=3]",
                 "3969": "minecraft:green_glazed_terracotta [\"facing_direction\"=4]",
                 "3970": "minecraft:green_glazed_terracotta [\"facing_direction\"=2]",
                 "3971": "minecraft:green_glazed_terracotta [\"facing_direction\"=5]",
                 "3984": "minecraft:red_glazed_terracotta [\"facing_direction\"=3]",
                 "3985": "minecraft:red_glazed_terracotta [\"facing_direction\"=4]",
                 "3986": "minecraft:red_glazed_terracotta [\"facing_direction\"=2]",
                 "3987": "minecraft:red_glazed_terracotta [\"facing_direction\"=5]",
                 "4000": "minecraft:black_glazed_terracotta [\"facing_direction\"=3]",
                 "4001": "minecraft:black_glazed_terracotta [\"facing_direction\"=4]",
                 "4002": "minecraft:black_glazed_terracotta [\"facing_direction\"=2]",
                 "4003": "minecraft:black_glazed_terracotta [\"facing_direction\"=5]",
                 "4016": "minecraft:concrete [\"color\"=\"white\"]",
                 "4017": "minecraft:concrete [\"color\"=\"orange\"]",
                 "4018": "minecraft:concrete [\"color\"=\"magenta\"]",
                 "4019": "minecraft:concrete [\"color\"=\"light_blue\"]",
                 "4020": "minecraft:concrete [\"color\"=\"yellow\"]", "4021": "minecraft:concrete [\"color\"=\"lime\"]",
                 "4022": "minecraft:concrete [\"color\"=\"pink\"]", "4023": "minecraft:concrete [\"color\"=\"gray\"]",
                 "4024": "minecraft:concrete [\"color\"=\"silver\"]", "4025": "minecraft:concrete [\"color\"=\"cyan\"]",
                 "4026": "minecraft:concrete [\"color\"=\"purple\"]", "4027": "minecraft:concrete [\"color\"=\"blue\"]",
                 "4028": "minecraft:concrete [\"color\"=\"brown\"]", "4029": "minecraft:concrete [\"color\"=\"green\"]",
                 "4030": "minecraft:concrete [\"color\"=\"red\"]", "4031": "minecraft:concrete [\"color\"=\"black\"]",
                 "4032": "minecraft:concrete_powder [\"color\"=\"white\"]",
                 "4033": "minecraft:concrete_powder [\"color\"=\"orange\"]",
                 "4034": "minecraft:concrete_powder [\"color\"=\"magenta\"]",
                 "4035": "minecraft:concrete_powder [\"color\"=\"light_blue\"]",
                 "4036": "minecraft:concrete_powder [\"color\"=\"yellow\"]",
                 "4037": "minecraft:concrete_powder [\"color\"=\"lime\"]",
                 "4038": "minecraft:concrete_powder [\"color\"=\"pink\"]",
                 "4039": "minecraft:concrete_powder [\"color\"=\"gray\"]",
                 "4040": "minecraft:concrete_powder [\"color\"=\"silver\"]",
                 "4041": "minecraft:concrete_powder [\"color\"=\"cyan\"]",
                 "4042": "minecraft:concrete_powder [\"color\"=\"purple\"]",
                 "4043": "minecraft:concrete_powder [\"color\"=\"blue\"]",
                 "4044": "minecraft:concrete_powder [\"color\"=\"brown\"]",
                 "4045": "minecraft:concrete_powder [\"color\"=\"green\"]",
                 "4046": "minecraft:concrete_powder [\"color\"=\"red\"]",
                 "4047": "minecraft:concrete_powder [\"color\"=\"black\"]",
                 "4080": "minecraft:structure_block [\"structure_block_type\"=\"save\"]",
                 "4081": "minecraft:structure_block [\"structure_block_type\"=\"load\"]",
                 "4082": "minecraft:structure_block [\"structure_block_type\"=\"corner\"]",
                 "4083": "minecraft:structure_block [\"structure_block_type\"=\"data\"]"}
def process_schematic(schematic_file, output_file):
    try:
        schematic = nbt.load(schematic_file)
        width = schematic['Width']
        height = schematic['Height']
        length = schematic['Length']
        blocks = schematic['Blocks']
        data = schematic['Data']

        with open(output_file, "w") as file:
            for y in range(height):
                for z in range(length):
                    for x in range(width):
                        index = x + (z * width) + (y * width * length)
                        block_name, block_data = block_names[blocks[index] & 0xFF], int(data[index])
                        if block_name != "air":
                            file.write(f"setblock ~{x} ~{y} ~{z} {block_name} {block_data}\n")

        messagebox.showinfo("Success", "转换完毕！")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}-牢底你的文件路径呢？")

def process_bdx(bdx_file, output_file):
    try:
        bdx = ReadBDXFile(bdx_file)
        with open(output_file, 'w+', encoding='utf-8') as file:
            file.write(f"#{bdx.AuthorName}\n")
            x, y, z = 0, 0, 0
            constantStrings = []

            for i in bdx.BDXContents:
                if i.operationNumber == 1:
                    constantStrings.append(i.constantString);
                elif (i.operationNumber == 14):
                    x += 1;
                elif (i.operationNumber == 15):
                    x -= 1;
                elif (i.operationNumber == 20 or i.operationNumber == 21 or i.operationNumber == 28):
                    x += i.value;
                elif (i.operationNumber == 16):
                    y += 1;
                elif (i.operationNumber == 17):
                    y -= 1;
                elif (i.operationNumber == 22 or i.operationNumber == 23 or i.operationNumber == 29):
                    y += i.value;
                elif (i.operationNumber == 18):
                    z += 1;
                elif (i.operationNumber == 19):
                    z -= 1;
                elif (
                        i.operationNumber == 24 or i.operationNumber == 25 or i.operationNumber == 30 or i.operationNumber == 8 or i.operationNumber == 12):
                    z += i.value;
                elif (i.operationNumber == 5):
                    file.write("setblock ~%d ~%d ~%d %s %s\n" % (
                    x, y, z, constantStrings[i.blockConstantStringID], constantStrings[i.blockStatesConstantStringID]));
                elif (i.operationNumber == 7):
                    file.write("setblock ~%d ~%d ~%d %s %d\n" % (
                    x, y, z, constantStrings[i.blockConstantStringID], i.blockData));
                elif (i.operationNumber == 9 or i.operationNumber == 88 or i.operationNumber == 69):
                    break;
                elif (i.operationNumber == 13):
                    file.write("setblock ~%d ~%d ~%d %s %s\n" % (
                    x, y, z, constantStrings[i.blockConstantStringID], i.blockStatesString));
                elif (i.operationNumber == 27):
                    file.write("setblock ~%d ~%d ~%d %s %d\n" % (
                    x, y, z, constantStrings[i.blockConstantStringID], i.blockData));
                elif (i.operationNumber == 36):
                    file.write("setblock ~%d ~%d ~%d command_block\n" % (x, y, z));
                elif (i.operationNumber == 41):
                    file.write("setblock ~%d ~%d ~%d %s %s\n" % (
                    x, y, z, constantStrings[i.blockConstantStringID], constantStrings[i.blockStatesConstantStringID]));
                elif (i.operationNumber == 39):
                    pass;
                else:
                    print("Unsupported operation number: %d" % (i.operationNumber));

        messagebox.showinfo("Success", "BDX 转换完毕")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}-牢底你的文件路径呢？")



#------------------txt优化部分------------------------------------
# #开始重构
def parse_state_string(block):

    state_string = ""
    if "states" in block:
        states = block["states"]
        for k, v in states.items():
            if state_string != "":
                state_string += ","
            if isinstance(v, str) and re.match(r"^\[.*\]$", v):
                state_string += f"\"{k}\":{v}"
            elif isinstance(v, int) or isinstance(v, float):
                state_string += f"\"{k}\":{v}"
            elif isinstance(v, str):
                state_string += f"\"{k}\":\"{v}\""
    return state_string

def is_continuous_region(blocks, x1, y1, z1, x2, y2, z2, block_name, state_string):

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                if (x, y, z) not in blocks or blocks[(x, y, z)][0] != block_name or blocks[(x, y, z)][1] != state_string:
                    return False
    return True

def find_largest_region(blocks, start, block_name, state_string):
#匹配区块
    x, y, z = start
    x_end, y_end, z_end = x, y, z

#寻找相邻
    while is_continuous_region(blocks, x, y, z, x_end + 1, y_end, z_end, block_name, state_string):
        x_end += 1
    while is_continuous_region(blocks, x, y, z, x_end, y_end + 1, z_end, block_name, state_string):
        y_end += 1
    while is_continuous_region(blocks, x, y, z, x_end, y_end, z_end + 1, block_name, state_string):
        z_end += 1

    return (x, y, z), (x_end, y_end, z_end)

def split_fill_command(start, end, block_name, state_string):

    x1, y1, z1 = start
    x2, y2, z2 = end
    block_count = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
#最大限制
    if block_count <= 32367:
        command = f"fill ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} {block_name}"
        if state_string:
            command += f" {state_string}"
        return [command]

    commands = []
    step = max(1, int(block_count ** (1 / 3)))
    for i in range(x1, x2 + 1, step):
        for j in range(y1, y2 + 1, step):
            for k in range(z1, z2 + 1, step):
                sub_x2 = min(i + step - 1, x2)
                sub_y2 = min(j + step - 1, y2)
                sub_z2 = min(k + step - 1, z2)
                commands.extend(split_fill_command((i, j, k), (sub_x2, sub_y2, sub_z2), block_name, state_string))
    return commands
#若无法三维次求二维、一维
def find_fill_regions(blocks):

    fill_commands = []
    setblock_commands = []
    block_count_3d = 0
    block_count_2d = 0
    block_count_1d = 0
    single_block_count = 0

    visited = set()
    for (x, y, z), (block_name, state_string) in blocks.items():
        if (x, y, z) in visited:
            continue

        start = (x, y, z)
        end = find_largest_region(blocks, start, block_name, state_string)
        x_end, y_end, z_end = end[1]

        region_size = (x_end - x + 1) * (y_end - y + 1) * (z_end - z + 1)
        if region_size > 1:
            fill_commands.extend(split_fill_command(start, end[1], block_name, state_string))
            if (x_end - x + 1) > 1 and (y_end - y + 1) > 1 and (z_end - z + 1) > 1:
                block_count_3d += region_size
            elif (x_end - x + 1) > 1 and (y_end - y + 1) > 1 or (z_end - z + 1) > 1:
                block_count_2d += region_size
            else:
                block_count_1d += region_size
        else:
            single_block_count += 1
            setblock_commands.append(f"setblock ~{x} ~{y} ~{z} {block_name} {state_string}")

        for x_visited in range(x, x_end + 1):
            for y_visited in range(y, y_end + 1):
                for z_visited in range(z, z_end + 1):
                    visited.add((x_visited, y_visited, z_visited))

    return fill_commands, setblock_commands, block_count_3d, block_count_2d, block_count_1d, single_block_count

def optimize_mcfunction(input_file, output_file):

    blocks = {}
    original_command_count = 0
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            original_command_count += 1
            if line.startswith('setblock'):
                parts = line.strip().split()
                x, y, z = int(parts[1][1:]), int(parts[2][1:]), int(parts[3][1:])
                block_name = parts[4]
                if len(parts) > 5:
                    state_string = ' '.join(parts[5:])
                else:
                    state_string = ""
                blocks[(x, y, z)] = (block_name, state_string)

    fill_commands, setblock_commands, block_count_3d, block_count_2d, block_count_1d, single_block_count = find_fill_regions(blocks)

    optimized_command_count = len(fill_commands) + len(setblock_commands)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for cmd in fill_commands:
            out_file.write(cmd + '\n')
        for cmd in setblock_commands:
            out_file.write(cmd + '\n')

    return (original_command_count, optimized_command_count, block_count_3d, block_count_2d, block_count_1d, single_block_count)


def merge_coordinates(input_file, output_file):
    def parse_data(line):
        data = line.strip().split()
        if len(data) == 4:
            data.append('')
        return data

    def merge_by_x(data_list):
        merged_data = []
        total_blocks = 0
        current_data = data_list[0]
        current_coords = (current_data[1], current_data[2], current_data[3])
        current_block = current_data[4]
        current_block1 = current_data[5] if len(current_data) > 5 else ''
        start_coords = current_coords
        end_coords = current_coords
        for data in data_list[1:]:
            coords = (data[1], data[2], data[3])
            block_type = data[4]
            block_type1 = data[5] if len(data) > 5 else ''
            if block_type != current_block or int(coords[0][1:]) != int(end_coords[0][1:]) + 1 or coords[2] != end_coords[2]:
                if start_coords == end_coords:
                    merged_data.append(f'setblock {start_coords[0]} {start_coords[1]} {start_coords[2]} {current_block} {current_block1}')
                    total_blocks += 1
                else:
                    merged_data.append(f'fill {start_coords[0]} {start_coords[1]} {start_coords[2]} {end_coords[0]} {end_coords[1]} {end_coords[2]} {current_block} {current_block1}')
                    total_blocks += (int(end_coords[0][1:]) - int(start_coords[0][1:]) + 1) * (int(end_coords[1][1:]) - int(start_coords[1][1:]) + 1) * (int(end_coords[2][1:]) - int(start_coords[2][1:]) + 1)
                current_block = block_type
                current_block1 = block_type1
                start_coords = coords
            end_coords = coords
        if start_coords == end_coords:
            merged_data.append(f'setblock {start_coords[0]} {start_coords[1]} {start_coords[2]} {current_block} {current_block1}')
            total_blocks += 1
        else:
            merged_data.append(f'fill {start_coords[0]} {start_coords[1]} {start_coords[2]} {end_coords[0]} {end_coords[1]} {end_coords[2]} {current_block} {current_block1}')
            total_blocks += (int(end_coords[0][1:]) - int(start_coords[0][1:]) + 1) * (int(end_coords[1][1:]) - int(start_coords[1][1:]) + 1) * (int(end_coords[2][1:]) - int(start_coords[2][1:]) + 1)
        return merged_data, total_blocks

    def merge_by_z(data_list):
        merged_data = []
        total_blocks = 0
        current_data = data_list[0]
        current_coords = (current_data[1], current_data[2], current_data[3])
        current_block = current_data[4]
        current_block1 = current_data[5] if len(current_data) > 5 else ''
        start_coords = current_coords
        end_coords = current_coords
        for data in data_list[1:]:
            coords = (data[1], data[2], data[3])
            block_type = data[4]
            block_type1 = data[5] if len(data) > 5 else ''
            if block_type != current_block or int(coords[2][1:]) != int(end_coords[2][1:]) + 1:
                if start_coords == end_coords:
                    merged_data.append(f'setblock {start_coords[0]} {start_coords[1]} {start_coords[2]} {current_block} {current_block1}')
                    total_blocks += 1
                else:
                    merged_data.append(f'fill {start_coords[0]} {start_coords[1]} {start_coords[2]} {end_coords[0]} {end_coords[1]} {end_coords[2]} {current_block} {current_block1}')
                    total_blocks += (int(end_coords[0][1:]) - int(start_coords[0][1:]) + 1) * (int(end_coords[1][1:]) - int(start_coords[1][1:]) + 1) * (int(end_coords[2][1:]) - int(start_coords[2][1:]) + 1)
                current_block = block_type
                current_block1 = block_type1
                start_coords = coords
            end_coords = coords
        if start_coords == end_coords:
            merged_data.append(f'setblock {start_coords[0]} {start_coords[1]} {start_coords[2]} {current_block} {current_block1}')
            total_blocks += 1
        else:
            merged_data.append(f'fill {start_coords[0]} {start_coords[1]} {start_coords[2]} {end_coords[0]} {end_coords[1]} {end_coords[2]} {current_block} {current_block1}')
            total_blocks += (int(end_coords[0][1:]) - int(start_coords[0][1:]) + 1) * (int(end_coords[1][1:]) - int(start_coords[1][1:]) + 1) * (int(end_coords[2][1:]) - int(start_coords[2][1:]) + 1)
        return merged_data, total_blocks

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data_points = [parse_data(line) for line in lines]

    grouped_data = {}
    for data in data_points:
        y_value = int(data[2][1:])
        if y_value not in grouped_data:
            grouped_data[y_value] = [data]
        else:
            grouped_data[y_value].append(data)

    merged_data = []
    total_blocks = 0

    for y_value, data_list in grouped_data.items():
        x_merged_data, x_total_blocks = merge_by_x(data_list)
        z_merged_data, z_total_blocks = merge_by_z(data_list)

        if len(x_merged_data) <= len(z_merged_data):
            merged_data.extend(x_merged_data)
            total_blocks += x_total_blocks
        else:
            merged_data.extend(z_merged_data)
            total_blocks += z_total_blocks


    min_x = min(int(data[1][1:]) for data in data_points)
    max_x = max(int(data[1][1:]) for data in data_points)
    min_y = min(int(data[2][1:]) for data in data_points)
    max_y = max(int(data[2][1:]) for data in data_points)
    min_z = min(int(data[3][1:]) for data in data_points)
    max_z = max(int(data[3][1:]) for data in data_points)


    ticking_areas = []
    step = 100
    for x in range(min_x, max_x + 1, step):
        for y in range(min_y, max_y + 1, step):
            for z in range(min_z, max_z + 1, step):
                area = f'tickingarea add ~{x} ~{y} ~{z} ~{x + step - 1} ~{y + step - 1} ~{z + step - 1}'
                ticking_areas.append(area)

    with open(output_file, 'w', encoding='utf-8') as f:
        for area in ticking_areas:
            f.write(area + '\n')
        for data in merged_data:
            f.write(data + '\n')

    original_time_minutes = len(data_points) * 0.1 / 60  # 原始导入时间计算，单位为分钟
    total_time_minutes = len(merged_data) * 0.1 / 60  # 合并后导入时间计算，单位为分钟

    return total_blocks, total_time_minutes, len(merged_data), original_time_minutes
#与此同时，另一边...
def merge_coordinates(input_file, output_file):
    def parse_data(line):
        data = line.strip().split()
        if len(data) == 4:
            data.append('')
        return data

    def merge_by_x(data_list):
        merged_data = []
        total_blocks = 0
        current_data = data_list[0]
        current_coords = (current_data[1], current_data[2], current_data[3])
        current_block = current_data[4]
        current_block1 = current_data[5] if len(current_data) > 5 else ''
        start_coords = current_coords
        end_coords = current_coords
        for data in data_list[1:]:
            coords = (data[1], data[2], data[3])
            block_type = data[4]
            block_type1 = data[5] if len(data) > 5 else ''
            if block_type != current_block or int(coords[0][1:]) != int(end_coords[0][1:]) + 1 or coords[2] != end_coords[2]:
                if start_coords == end_coords:
                    merged_data.append(f'setblock {start_coords[0]} {start_coords[1]} {start_coords[2]} {current_block} {current_block1}')
                    total_blocks += 1
                else:
                    merged_data.append(f'fill {start_coords[0]} {start_coords[1]} {start_coords[2]} {end_coords[0]} {end_coords[1]} {end_coords[2]} {current_block} {current_block1}')
                    total_blocks += (int(end_coords[0][1:]) - int(start_coords[0][1:]) + 1) * (int(end_coords[1][1:]) - int(start_coords[1][1:]) + 1) * (int(end_coords[2][1:]) - int(start_coords[2][1:]) + 1)
                current_block = block_type
                current_block1 = block_type1
                start_coords = coords
            end_coords = coords
        if start_coords == end_coords:
            merged_data.append(f'setblock {start_coords[0]} {start_coords[1]} {start_coords[2]} {current_block} {current_block1}')
            total_blocks += 1
        else:
            merged_data.append(f'fill {start_coords[0]} {start_coords[1]} {start_coords[2]} {end_coords[0]} {end_coords[1]} {end_coords[2]} {current_block} {current_block1}')
            total_blocks += (int(end_coords[0][1:]) - int(start_coords[0][1:]) + 1) * (int(end_coords[1][1:]) - int(start_coords[1][1:]) + 1) * (int(end_coords[2][1:]) - int(start_coords[2][1:]) + 1)
        return merged_data, total_blocks

    def merge_by_z(data_list):
        merged_data = []
        total_blocks = 0
        current_data = data_list[0]
        current_coords = (current_data[1], current_data[2], current_data[3])
        current_block = current_data[4]
        current_block1 = current_data[5] if len(current_data) > 5 else ''
        start_coords = current_coords
        end_coords = current_coords
        for data in data_list[1:]:
            coords = (data[1], data[2], data[3])
            block_type = data[4]
            block_type1 = data[5] if len(data) > 5 else ''
            if block_type != current_block or int(coords[2][1:]) != int(end_coords[2][1:]) + 1:
                if start_coords == end_coords:
                    merged_data.append(f'setblock {start_coords[0]} {start_coords[1]} {start_coords[2]} {current_block} {current_block1}')
                    total_blocks += 1
                else:
                    merged_data.append(f'fill {start_coords[0]} {start_coords[1]} {start_coords[2]} {end_coords[0]} {end_coords[1]} {end_coords[2]} {current_block} {current_block1}')
                    total_blocks += (int(end_coords[0][1:]) - int(start_coords[0][1:]) + 1) * (int(end_coords[1][1:]) - int(start_coords[1][1:]) + 1) * (int(end_coords[2][1:]) - int(start_coords[2][1:]) + 1)
                current_block = block_type
                current_block1 = block_type1
                start_coords = coords
            end_coords = coords
        if start_coords == end_coords:
            merged_data.append(f'setblock {start_coords[0]} {start_coords[1]} {start_coords[2]} {current_block} {current_block1}')
            total_blocks += 1
        else:
            merged_data.append(f'fill {start_coords[0]} {start_coords[1]} {start_coords[2]} {end_coords[0]} {end_coords[1]} {end_coords[2]} {current_block} {current_block1}')
            total_blocks += (int(end_coords[0][1:]) - int(start_coords[0][1:]) + 1) * (int(end_coords[1][1:]) - int(start_coords[1][1:]) + 1) * (int(end_coords[2][1:]) - int(start_coords[2][1:]) + 1)
        return merged_data, total_blocks

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data_points = [parse_data(line) for line in lines]

    grouped_data = {}
    for data in data_points:
        y_value = int(data[2][1:])
        if y_value not in grouped_data:
            grouped_data[y_value] = [data]
        else:
            grouped_data[y_value].append(data)

    merged_data = []
    total_blocks = 0

    for y_value, data_list in grouped_data.items():
        x_merged_data, x_total_blocks = merge_by_x(data_list)
        z_merged_data, z_total_blocks = merge_by_z(data_list)

        if len(x_merged_data) <= len(z_merged_data):
            merged_data.extend(x_merged_data)
            total_blocks += x_total_blocks
        else:
            merged_data.extend(z_merged_data)
            total_blocks += z_total_blocks


    min_x = min(int(data[1][1:]) for data in data_points)
    max_x = max(int(data[1][1:]) for data in data_points)
    min_y = min(int(data[2][1:]) for data in data_points)
    max_y = max(int(data[2][1:]) for data in data_points)
    min_z = min(int(data[3][1:]) for data in data_points)
    max_z = max(int(data[3][1:]) for data in data_points)


    ticking_areas = []
    step = 100
    for x in range(min_x, max_x + 1, step):
        for y in range(min_y, max_y + 1, step):
            for z in range(min_z, max_z + 1, step):
                area = f'tickingarea add ~{x} ~{y} ~{z} ~{x + step - 1} ~{y + step - 1} ~{z + step - 1}'
                ticking_areas.append(area)

    with open(output_file, 'w', encoding='utf-8') as f:
        for area in ticking_areas:
            f.write(area + '\n')
        for data in merged_data:
            f.write(data + '\n')

    original_time_minutes = len(data_points) * 0.1 / 60
    total_time_minutes = len(merged_data) * 0.1 / 60
    pass

#----------------------------------------界面调整-------------------------Ciallo～(∠・ω< )⌒★


def run_merge(merge_result_label=None):
    input_file = input_merge_entry.get()
    output_file = output_merge_entry.get()

    if not input_file or not output_file:
        messagebox.showwarning("Input Error", "不是哥们，文件路径你没放全啊")
        return

    total_blocks, total_time_minutes, total_commands, original_time_minutes = merge_coordinates(input_file, output_file)

    result_text1 = f'原命令数量: {total_blocks}\n'
    result_text1 += f'原导入预计时间: {original_time_minutes:.2f} minutes\n'
    result_text1 += f'二维合并后命令数量: {total_commands}\n'
    result_text1 += f'二维合并后导入预计时间: {total_time_minutes:.2f} minutes\n'

    merge_result_label.config(text=result_text1)


def select_input_merge():
    input_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    input_merge_entry.delete(0, tk.END)
    input_merge_entry.insert(0, input_file)

def select_output_merge():
    output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    output_merge_entry.delete(0, tk.END)
    output_merge_entry.insert(0, output_file)

#bdx

def ReadBDXFile(path: str) -> BDX:
    with open(path, "r+b") as file:
        fileContext: bytes = file.read()
    result = BDX()
    result.UnMarshal(fileContext)
    return result

def select_schematic_file():
    file_path = filedialog.askopenfilename(title="Select Schematic File", filetypes=[("Schematic Files", "*.schematic")])
    schematic_file_var.set(file_path)

def select_bdx_file():
    file_path = filedialog.askopenfilename(title="Select BDX File", filetypes=[("BDX Files", "*.bdx")])
    bdx_file_var.set(file_path)

def select_output_file(var):
    file_path = filedialog.asksaveasfilename(title="Save Output File", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    var.set(file_path)

def run_schematic_processing():
    process_schematic(schematic_file_var.get(), schematic_output_var.get())

def run_bdx_processing():
    process_bdx(bdx_file_var.get(), bdx_output_var.get())


def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text or MCFunction files", "*.txt *.mcfunction")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text or MCFunction files", "*.txt *.mcfunction")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def run_optimization():
    input_file = input_entry.get()
    output_file = output_entry.get()

    if not input_file or not output_file:
        messagebox.showerror("错误", "不是哥们，输入和输出文件路径你不填，你来转牛魔呢")
        return

    try:
        original_count, optimized_count, block_3d, block_2d, block_1d, single_blocks = optimize_mcfunction(input_file, output_file)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"[三维优化] 可优化命令数量：{block_3d}\n")
        result_text.insert(tk.END, f"[二维优化] 可优化命令数量：{block_2d}\n")
        result_text.insert(tk.END, f"[一维优化] 可优化命令数量：{block_1d}\n")
        result_text.insert(tk.END, f"[单个方块命令数量]：{single_blocks}\n")
        result_text.insert(tk.END, f"原始命令总数：{original_count}\n")
        result_text.insert(tk.END, f"优化后命令总数：{optimized_count}\n")
    except Exception as e:
        messagebox.showerror("错误", f"优化过程中出错：{e}-特征匹配出错，牢底你这文件不保熟啊")

def show_protection_message():
    messagebox.showwarning(
        "版权声明",
        "版权所有：雾已散_声声慢 q:1579103236\n\n请尊重作者的知识产权，感谢您的支持。\n\n本项目开源，如果这还能有倒卖仔当老鼠\n\n就请呆在你的下水道里别让我发现"
    )


root = tk.Tk()
root.title("雾已散_声声慢-转换优化综合处理器-q:1579103236")
root.geometry("1200x800")

root.after(100, show_protection_message)


bg_image = Image.open("bk.jpg")
bg_image = bg_image.resize((1200, 800), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


top_frame = tk.Frame(root, bg="white")
top_frame.place(relx=0.16, rely=0.87, anchor="n")

label_author = tk.Label(top_frame, text="作者: 雾已散_声声慢", font=("Arial", 14), fg=random_color(), bg="white")
label_author.grid(row=0, column=0)

label_q = tk.Label(top_frame, text="q：1579103236", font=("Arial", 12), fg=random_color(), bg="white")
label_q.grid(row=1, column=0)


top_frame1 = tk.Frame(root, bg="white")
top_frame1.place(relx=0.84, rely=0.87, anchor="n")

label_author = tk.Label(top_frame1, text="作者: 雾已散_声声慢", font=("Arial", 14), fg=random_color(), bg="white")
label_author.grid(row=0, column=0)

label_q = tk.Label(top_frame1, text="q：1579103236", font=("Arial", 12), fg=random_color(), bg="white")
label_q.grid(row=1, column=0)


bottom_label = tk.Label(root, text="如果你是花钱买的，我只能说冤种的奖池还在累积", font=("Arial", 13), fg=random_color(), bg="white")
bottom_label.place(relx=0.5, rely=1, anchor="s")


schematic_file_var = tk.StringVar()
schematic_output_var = tk.StringVar()
bdx_file_var = tk.StringVar()
bdx_output_var = tk.StringVar()


merge_frame = tk.Frame(root, padx=10, pady=10, bg="white")
merge_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

tk.Label(merge_frame, text="一维优化（适合十万以下的文件，处理快，命令压缩效率3-7倍）", font=("Arial", 14), fg=random_color(), bg="white").grid(row=0, column=0, columnspan=3)


input_merge_label = tk.Label(merge_frame, text="输入文件：")
input_merge_label.grid(row=1, column=0, padx=5, pady=5)
input_merge_entry = tk.Entry(merge_frame, width=40)
input_merge_entry.grid(row=1, column=1, padx=5, pady=5)
input_merge_btn = tk.Button(merge_frame, text="选择文件", command=lambda: select_input_merge())
input_merge_btn.grid(row=1, column=2, padx=5, pady=5)


output_merge_label = tk.Label(merge_frame, text="输出文件：")
output_merge_label.grid(row=2, column=0, padx=5, pady=5)
output_merge_entry = tk.Entry(merge_frame, width=40)
output_merge_entry.grid(row=2, column=1, padx=5, pady=5)
output_merge_btn = tk.Button(merge_frame, text="选择文件", command=lambda: select_output_merge())
output_merge_btn.grid(row=2, column=2, padx=5, pady=5)


run_merge_btn = tk.Button(merge_frame, text="运行一维优化", command=lambda: run_merge())
run_merge_btn.grid(row=5, column=1, padx=5, pady=5)


schematic_frame = tk.Frame(root, padx=10, pady=10, bg="white")
schematic_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

tk.Label(schematic_frame, text="Schematic转换为Txt", font=("Arial", 14), fg=random_color(), bg="white").grid(row=0, column=0, columnspan=3)

tk.Button(schematic_frame, text="选择输入文件", command=lambda: select_schematic_file()).grid(row=1, column=0, padx=5, pady=5)
tk.Entry(schematic_frame, textvariable=schematic_file_var, width=50).grid(row=1, column=1, padx=5, pady=5)

tk.Button(schematic_frame, text="选择输出文件", command=lambda: select_output_file(schematic_output_var)).grid(row=2, column=0, padx=5, pady=5)
tk.Entry(schematic_frame, textvariable=schematic_output_var, width=50).grid(row=2, column=1, padx=5, pady=5)

tk.Button(schematic_frame, text="开始运算", command=lambda: run_schematic_processing()).grid(row=3, column=1, padx=5, pady=5)


bdx_frame = tk.Frame(root, padx=10, pady=10, bg="white")
bdx_frame.grid(row=1, column=0, sticky="nw", padx=10, pady=10)

tk.Label(bdx_frame, text="BDX转换为Txt", font=("Arial", 14), fg=random_color(), bg="white").grid(row=0, column=0, columnspan=3)

tk.Button(bdx_frame, text="选择输入文件", command=lambda: select_bdx_file()).grid(row=1, column=0, padx=5, pady=5)
tk.Entry(bdx_frame, textvariable=bdx_file_var, width=50).grid(row=1, column=1, padx=5, pady=5)

tk.Button(bdx_frame, text="选择输出文件", command=lambda: select_output_file(bdx_output_var)).grid(row=2, column=0, padx=5, pady=5)
tk.Entry(bdx_frame, textvariable=bdx_output_var, width=50).grid(row=2, column=1, padx=5, pady=5)

tk.Button(bdx_frame, text="开始运算", command=lambda: run_bdx_processing()).grid(row=3, column=1, padx=5, pady=5)

frame_mcfunction = tk.Frame(root, padx=10, pady=10, bg="white")
frame_mcfunction.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

tk.Label(frame_mcfunction, text="三维优化（适合千万级别的文件，处理慢，命令压缩效率10-30倍）", font=("Arial", 14), fg=random_color(), bg="white").grid(row=0, column=0, columnspan=3)

input_label = tk.Label(frame_mcfunction, text="输入文件：")
input_label.grid(row=1, column=0, padx=5, pady=5)

input_entry = tk.Entry(frame_mcfunction, width=40)
input_entry.grid(row=1, column=1, padx=5, pady=5)

input_button = tk.Button(frame_mcfunction, text="选择文件", command=lambda: select_input_file())
input_button.grid(row=1, column=2, padx=5, pady=5)

output_label = tk.Label(frame_mcfunction, text="输出文件：")
output_label.grid(row=2, column=0, padx=5, pady=5)

output_entry = tk.Entry(frame_mcfunction, width=40)
output_entry.grid(row=2, column=1, padx=5, pady=5)

output_button = tk.Button(frame_mcfunction, text="选择文件", command=lambda: select_output_file())
output_button.grid(row=2, column=2, padx=5, pady=5)

run_button = tk.Button(frame_mcfunction, text="运行优化", command=lambda: run_optimization())
run_button.grid(row=6, column=1, padx=5, pady=5)


result_text = scrolledtext.ScrolledText(frame_mcfunction, width=60, height=10)
result_text.grid(row=3, column=0, columnspan=3, padx=5, pady=5)


root.mainloop()

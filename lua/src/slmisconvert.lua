json = require "json"
dofile("lua/src/config.lua")

stats_path = arg[1]
--save_path = paths["savedir"]

dofile(stats_path)
JSON = assert(loadfile "lua/src/JSON.lua")() -- one-time load of the routines

local stats_json = JSON:encode_pretty(misStats) -- "pretty printed" version for human readability
--local currentLocalTime= os.date('%Y-%m-%d-%H%M%S')


local filename= "".. paths["misstats"] .. "" .. arg[2] .. ".json"
file = io.open(filename,"w")
io.output(file)
io.write(stats_json)
io.close(file)
print("Saved SLMod mission file as JSON at ...")
print(filename)
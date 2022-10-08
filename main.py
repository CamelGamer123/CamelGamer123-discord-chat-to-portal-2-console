import discord
import os

token = "Token goes here"
ip = "Ip goes here"
port = "54321"
channel = Channelid goes here

prefix = "mirror "
banned = ["ent_create player", "snd_restart", "cl_timeout", "cl_ignorepackets", "fire_rocket_projectile", "killserver",
          "sv_cheats", "ch_createjalopy", "disconnect", "setpos", "noclip", "ent_fire @transition", "mat_", "_restart",
          "quit", "load", "ghost_", "alias", "bench_", "benchframe", "cam_", "camortho", "changelevel",
          "connect", "crash", "demo_", "demos", "editdemo", "editor_toggle", "ent_pause", "exit", "exec",
          "execifexists", "filesystem_", "forcebind", "fps_", "func_", "g_", "hammer_", "host_", "hostfile", "hostup",
          "hostname", "hostport", "hidehud", "m_", "mat_aaquality ", "mat_antialias", "mem_", "cpu_", "gpu_", "mod_",
          "+mouse_", "movie_", "mp_", "nav_", "net_", "next", "nextdemo", "nextlevel", "particle_", "phys_", "physics_",
          "playdemo", "plugin_", "r_", "rcon", "rcon_", "recompute_speed", "record", "rope_", "rr_", "scene_",
          "setmodel", "singlestep ", "spike", "ss_", "star_memory", "startdemos", "startmovie", "startneurotoxins",
          "startupmenu", "+strafe", "sv_allow", "sv_benchmark", "swap_ss_input ", "sys_", "test_", "timedemo",
          "timedemo_vprofrecord", "timedemo_quit", "timerefresh", "toolload", "toolunload", "tv_",
          "unbindall", "unload_all_addons", "update_addon_paths ", "v_", "vgui_", "viewanim_", "viper_bug", "vprof_",
          "vtune", "vx_", "wc_", "wipe_", "mat_wireframe", "map", "sar_", "benchmark", "destroy()",
          "point_servercommand", "lightprobe", "benchmark", "restart", "ban", "delta", "download", "reload", "render",
          "debug", "software", "texture", "print", "vol", "sendtoconsole", "quit", "kill"]


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author} in {message.channel.id}: {message.content}')
        if message.content in banned:
            print("This message is banned")
        elif message.author == client.user:
            print("Message from self ignored")
        else:
            print("This message is not banned")
            if message.channel.id == channel:
                print("This is in the right channel")
                if prefix in message.content:
                    print("The Prefix is in the message content")
                    inp = message.content

                    command = inp.removeprefix(prefix)
                    os.system(f"echo {command} | ncat {ip} {port}")

                    client.get_channel(channel)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)

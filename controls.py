from flask import Flask, jsonify
import jsonrpclib

from maraschino import app
from settings import *
from noneditable import *
from tools import *

@app.route('/xhr/play_episode/<int:episode_id>')
@requires_auth
def xhr_play_episode(episode_id):
    xbmc = jsonrpclib.Server(server_api_address())
    xbmc.Playlist.Clear(playlistid=1)

    item = { 'episodeid': episode_id }
    xbmc.Playlist.Add(playlistid=1, item=item)

    item = { 'playlistid': 1 }
    xbmc.Player.Open(item)

    return jsonify({ 'success': True })

@app.route('/xhr/play_movie/<int:movie_id>')
@requires_auth
def xhr_play_movie(movie_id):
    xbmc = jsonrpclib.Server(server_api_address())
    xbmc.Playlist.Clear(playlistid=1)

    item = { 'movieid': movie_id }
    xbmc.Playlist.Add(playlistid=1, item=item)

    item = { 'playlistid': 1 }
    xbmc.Player.Open(item)

    return jsonify({ 'success': True })

@app.route('/xhr/controls/<command>')
@requires_auth
def xhr_controls(command):
    xbmc = jsonrpclib.Server(server_api_address())

    if command == 'play_pause':
        xbmc.Player.PlayPause(playerid=1)

    elif command == 'stop':
        xbmc.Player.Stop(playerid=1)

    elif command == 'update_video':
    	xbmc.VideoLibrary.Scan()
	
    elif command == 'clean_video':
    	xbmc.VideoLibrary.Clean()

    elif command == 'update_audio':
        xbmc.AudioLibrary.Scan()

    elif command == 'clean_audio':
        xbmc.AudioLibrary.Clean()
    	
    return jsonify({ 'success': True })

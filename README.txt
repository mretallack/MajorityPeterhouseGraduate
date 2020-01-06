This is an initial reverse engineer of the protocol used for remote control of the Majority Peterhouse Graduate internet radio. 


The "Server" is magic iradio

There are a number of HTTP end points:

/play_url?id=8_1

Gets the URL for the stream


/play_stn?id=8_1

Starts playing the stream


/playinfo

Returns the info about what is playing. 



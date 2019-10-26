#!/usr/bin/env micropython

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import ColorSensor

tank = MoveTank(OUTPUT_A, OUTPUT_B)
#tank.on_for_rotations(50, 75, 0.5)



tank.cs = ColorSensor()

try:
    # Follow the line for 4500ms
    kp = 3
    ki = 0.01
    kd = 0

    dt = 2.2*1000

    tank.follow_line(
        target_light_intensity=None,
        kp=kp, ki=ki, kd=kd,
        speed=SpeedPercent(45),
        white=60,
        follow_for=follow_for_ms,
        ms=dt
    )
except Exception:
    tank.stop()
    raise
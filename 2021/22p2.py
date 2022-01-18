import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Cuboid:
    xs: int
    xe: int
    ys: int
    ye: int
    zs: int
    ze: int

    def area(self):
        return (self.xe - self.xs) * (self.ye - self.ys) * (self.ze - self.zs)

    def intersect(self, sub):
        return (
            self.xs < sub.xe
            and self.ys < sub.ye
            and self.zs < sub.ze
            and self.xe > sub.xs
            and self.ye > sub.ys
            and self.ze > sub.zs
        )

    def slice(self, sub):
        if not self.intersect(sub):
            yield self
        else:
            sub = Cuboid(
                min(max(sub.xs, self.xs), self.xe),
                min(max(sub.xe, self.xs), self.xe),
                min(max(sub.ys, self.ys), self.ye),
                min(max(sub.ye, self.ys), self.ye),
                min(max(sub.zs, self.zs), self.ze),
                min(max(sub.ze, self.zs), self.ze),
            )

            yield Cuboid(self.xs, sub.xs, self.ys, self.ye, self.zs, self.ze)
            yield Cuboid(sub.xe, self.xe, self.ys, self.ye, self.zs, self.ze)
            yield Cuboid(sub.xs, sub.xe, self.ys, sub.ys, self.zs, self.ze)
            yield Cuboid(sub.xs, sub.xe, sub.ye, self.ye, self.zs, self.ze)
            yield Cuboid(sub.xs, sub.xe, sub.ys, sub.ye, self.zs, sub.zs)
            yield Cuboid(sub.xs, sub.xe, sub.ys, sub.ye, sub.ze, self.ze)


cubes = []
for step in sys.stdin.read().split("\n"):
    xr, yr, zr = [list(map(int, s.split("=")[-1].split(".."))) for s in step.split(",")]
    step_cube = Cuboid(xr[0], xr[1] + 1, yr[0], yr[1] + 1, zr[0], zr[1] + 1)
    cubes = [sub for cube in cubes for sub in cube.slice(step_cube) if sub.area()]
    if "on" in step:
        cubes.append(step_cube)

print(sum([c.area() for c in cubes]))

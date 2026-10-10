# SPDX-License-Identifier: MPL-2.0
"""Research-only earned facts with explicit provenance, not inferred hypotheses."""


class Knowledge:
    def __init__(self):
        self.pairs = {}
        self.mixtures = []

    def observe(self, edge, stable, source):
        edge = tuple(edge)
        if len(edge) != 3 or edge[0] not in ('PF', 'FE') or type(stable) is not bool:
            raise ValueError('Invalid pair observation')
        if edge in self.pairs and self.pairs[edge]['stable'] != stable:
            raise ValueError('Contradictory earned fact')
        record = self.pairs.setdefault(edge, dict(stable=stable, sources=[]))
        if source not in record['sources']:
            record['sources'].append(source)

    def mixture(self, components, success, source):
        components = tuple(components)
        if len(components) not in (2, 3) or type(success) is not bool:
            raise ValueError('Invalid mixture record')
        self.mixtures.append(dict(components=components, success=success, source=source))
        if success and len(components) == 3:
            p, f, e = components
            self.observe(('PF', p, f), True, source)
            self.observe(('FE', f, e), True, source)

    def priors(self, relevant=None, stable_only=False):
        return {e: row['stable'] for e, row in self.pairs.items()
                if (relevant is None or e in relevant) and (not stable_only or row['stable'])}

    def snapshot(self):
        return dict(pairs=[dict(edge=list(e), **row) for e, row in sorted(self.pairs.items())],
                    mixtures=list(self.mixtures))

    @classmethod
    def restore(cls, data):
        result = cls()
        # Replay explicit facts only; restoring mixture history must not fabricate
        # additional provenance or accidentally turn a failed triple into edges.
        for row in data['pairs']:
            for source in row['sources']:
                result.observe(row['edge'], row['stable'], source)
        result.mixtures = [dict(row, components=tuple(row['components'])) for row in data['mixtures']]
        return result

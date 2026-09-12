from viva_munk import core_import


def build_core(core=None):
    """Return a bigraph-schema core with viva_munk's types + processes registered.

    Uniform cross-repo signature: pass an existing ``core`` to COMPOSE viva_munk's
    registrations onto it (so a downstream repo's build_core can inherit them);
    omit it to get a fresh core. Thin wrapper over ``core_import(core=None)``.
    """
    return core_import(core)

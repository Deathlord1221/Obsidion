"""The checks in this module run on every command."""


def init_global_checks(bot):
    @bot.check_once
    def minimum_bot_perms(ctx) -> bool:
        """
        Too many 403, 401, and 429 Errors can cause bots to get global'd
        It's reasonable to assume the below as a minimum amount of perms for
        commands.
        """
        return ctx.channel.permissions_for(ctx.me).send_messages

    @bot.check_once
    def bots(ctx) -> bool:
        """Check the user is not another bot."""
        return not ctx.author.bot

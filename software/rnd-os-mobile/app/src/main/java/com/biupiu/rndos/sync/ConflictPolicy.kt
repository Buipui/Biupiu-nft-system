package com.biupiu.rndos.sync

enum class ConflictPolicy { PRESERVE_SERVER_RECORD, PRESERVE_LOCAL_DRAFT, REQUIRE_REVIEW }

object DefaultConflictPolicy {
    val policy = ConflictPolicy.REQUIRE_REVIEW
}

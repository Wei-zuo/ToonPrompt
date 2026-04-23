from __future__ import annotations

from pathlib import Path

from runtime.video_agents.assets import Asset, AssetLibrary


def test_asset_library_load_save_and_resolve_name(tmp_path: Path) -> None:
    root = tmp_path / "assets"
    library = AssetLibrary(root)
    library.add(
        Asset(
            asset_id="luban",
            asset_type="character",
            name="鲁班",
            aliases=["鲁师傅"],
            description="匠人",
            visual_hooks=["石锤"],
            reference_image_paths=["character/luban/luban-001.png"],
            status="approved",
            created_by_phase="art_design",
            created_by_agent="image_production",
            notes="",
        )
    )
    library.add(
        Asset(
            asset_id="bridge",
            asset_type="location",
            name="赵州桥",
            aliases=["石桥", "桥"],
            description="石拱桥",
            visual_hooks=["青灰石拱"],
            reference_image_paths=["location/bridge/bridge-001.png"],
            status="approved",
            created_by_phase="art_design",
            created_by_agent="image_production",
            notes="",
        )
    )
    library.save()

    reloaded = AssetLibrary(root).load()
    assert reloaded.get("luban") is not None
    assert reloaded.find_by_name("鲁班").asset_id == "luban"
    assert reloaded.find_by_alias("石桥").asset_id == "bridge"
    assert [asset.asset_id for asset in reloaded.resolve_name("鲁班走上桥，摸了摸赵州桥。")] == ["luban", "bridge"]

    reloaded.update_status("luban", "generated")
    assert reloaded.get("luban").status == "generated"
